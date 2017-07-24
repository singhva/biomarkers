/**
 * This function brings up the pubmed form editing popup dialog
 */
$.fn.popUpEdit = function(form) {
	var self = $(this);
	var td = self.parents("td");
	var div = $("#form-holder-div");
	var pmid = $(form).attr("id").substring(5);
	var tab_content = $(form).find(".tab-content");
	tab_content.attr("id", tab_content.attr("id")+pmid);	
	
	$(form).find(".nav.nav-tabs a").each(function(){
		var data_target = $(this).attr("data-target");
		data_target = "#tab-content-" + pmid + data_target;
		$(this).attr("data-target", data_target);
	});
	
	div.find(".ui-widget").html(form);
	div.dialog("open");
	
	/*
	self.removeAttr("onclick");
	
	self.click(function() {
		self.parents("td").find(".form-holder-div").dialog('open');
	});
	
	*/
	
	/*
	div.dialog({
	      height: 600,
	      width: 1000,
	      modal: true,
	      appendTo: td,
	      create: function(event, ui){
	    	  	var html = "<span class='title'>Publication details&nbsp;<span class='glyphicon glyphicon-lock'></span></span><br>";
	    	  	var a = document.createElement("a");
	    	  	a.href = "javascript:void(0)";
	    	  	a.style.fontSize = "10px";
	    	  	a.innerHTML = "Read abstract";
				$(this).dialog('widget').find("span.ui-dialog-title").html(html).append(a);
				a.onclick = function() {
					$('#read-abstract-dialog').dialog('open');
				};
		  },
	      buttons: [
	                {text: 'Edit', class: 'btn btn-link'},
	                {text: 'Save', class: 'btn btn-primary', click: function() {submitCuratedForm(form)}},
	                {text: "Cancel", class:"btn btn-danger", click: function() { $(this).dialog("close"); }}
	      ]
	});
	*/
};

/**
 * This function fills the information in the popup form dialog
 * @param form
 * @param data
 */
function createFormData(form, data) {
	//form.find("input[name='abstract']").val(data["abstract"]);
	$('#read-abstract-dialog > p').html(data["abstract"]);
	$('#read-abstract-dialog').attr("data-pmid", data["pmid"]);
	$('#read-abstract-dialog').attr("title", "Abstract (PMID: " + data["pmid"] + ")");
	var annotations = data["annotations"];
	var disease_annotations = annotations["diseases"]["USER"];
	for (var i = 0; i < disease_annotations.length; i++) {
		var mentions = disease_annotations[i]["MENTIONS"];
		for (var j = 0; j < mentions.length; j++) {
			var text = mentions[j]["TEXT"];
			var startOffset = mentions[j]["START_POS"];
			var endOffset = mentions[j]["END_POS"];
			console.log("startOffset: "+startOffset+", endOffset: "+endOffset);
			
			createAnnotatedText(startOffset, endOffset, 
					document.getElementById("read-abstract-dialog").getElementsByTagName("p").item(0).firstChild, // Text Node
					function() {	 // Needs to be fixed		
						$('#read-abstract-dialog').data("range", { "text" : "123", "startOffset" : startOffset, "endOffset" : endOffset });
						$("#enter-disease-name-dialog").dialog("open");
					}
			);
		}
	}
	//form.find("p[data-name='article-title']").html(data.title);
	
	/*********************** Clinical Trial IDs  ******************************/
	form.find("input[name='trial_ids']").select2({
		placeholder: "Enter a valid 11-character clinical trial ID",
		minimumInputLength: 11,
		multiple: true,
		initSelection: function (item, callback) {
			var data1 = [];
			for(var i = 0; i < data.trial_ids.length; i++) {
				data1.push({id:data.trial_ids[i], text:data.trial_ids[i], locked: true});
			}
			callback(data1);
		},
		ajax:{
			url:"lookups/validate_trial_ids",
			dataType: "json",
			quietMillis: 500,
			data: function (term, page) {
	            return {
	                q: term, // search term
	            };
	        },
			results: function (data, page) {				
				return {results: data};
	        }
		}
	}).select2("val", Object.keys(data.trial_ids));
	/**************************************************************************/
	
	/*********************** Clinical Trial Type  *****************************/
	/*
	form.find("select[name='trial_info'] > option").each(function() {
		var index = data.trial_info.indexOf($(this).html());
		if (index > -1) $(this).attr("selected", "true");
		else $(this).removeAttr("selected");
	});
	*/
	form.find("select[name='trial_info']").select2().select2("val", data.trial_info);
	/**************************************************************************/
		
	/************************ Publication Type  *******************************/
	/*
	form.find("select[name='publication_types'] > option").each(function() {
		var index = data.publication_types.indexOf($(this).html());
		if (index > -1) $(this).attr("selected", "true");
		else $(this).removeAttr("selected");
	});
	*/
	form.find("select[name='publication_types']").select2().select2("val", data.publication_types);
	/**************************************************************************/
	
	/*************************** Cancer Type  *********************************/
	//alert(data["diseases"][0]["normalized_text"]);
		console.log($(this).attr("name"));
		var name = $(this).attr("name");
		var selected_disease_ids = [];
		var diseases_data = data["annotations"]["diseases"]["SYSTEM"];
		$.each(diseases_data, function(index, value) {
			selected_disease_ids.push(value["DB_ID"]);
		});
		console.log(diseases_data);
		form.find("input[name^='disease_annotations_nlp']").select2({
			placeholder: "Search for a cancer type",
			minimumInputLength: 3,
			multiple: true,
			initSelection: function (item, callback) {
				var data1 = [];
				for (var i = 0; i < diseases_data.length; i++) {
					data1.push({id: diseases_data[i]["DB_ID"], text: diseases_data[i]["NORMALIZED"], title : "TITLE"});
				}
				callback(data1);
			},
			formatSelectionCssClass : function (object, container){
				
			},
			formatSelection : function (object, container){
				return "<a href='#' class='select-option-tooltip' title='"+object["title"]+"'>"+object["text"]+"</a>";
			},
			ajax:{
				url: base + "/lookups/autocomplete_cancer_type",
				dataType: "json",
				quietMillis: 500,
				data: function (term, page) {
		            return {
		                q: term, // search term
		            };
		        },
				results: function (data, page) {
		            return {results: data};
		        }
			}
		}).select2("val", selected_disease_ids);
	
	//form.find("select[name='cancer_type_manual']").append("<option>"+data["diseases"][0]["normalized_text"]+"</option>");
	
	/**************************************************************************/
	
	//var drugs_table = form.find("table[data-name='drugs']");
	var html = "";
	
	for(var drug_id in data.drugs) {
		html += "<tr>";
		html += "<td>"+data.drugs[drug_id]+"</td>";
		html += "<td>";
		html += "<input type='checkbox' checked name='"+drug_id+"' class='like-or-dislike' value='-1' />";
		html += "</td>";
		html += "<td><button type='button' class='close' aria-hidden='true' onclick=\"$(this).parent().parent().remove()\">&times;</button></td>";
		html += "</tr>";
	}
	
	form.find("table[data-name='drugs'] > tbody").append(html).find(".like-or-dislike").likeOrDislike();
	
	var drug_name_input = form.find("input[name='enter_drug_name']");
	drug_name_input.autocomplete({
		source: base + "/lookups/autocomplete_drug_names",
		minLength: 3,
		delay: 500,
		appendTo: drug_name_input.parent(),
		select: function(event, ui) {
			var html = "<tr>";
			html += "<td>"+ui.item.label+"</td>";
			html += "<td>";
			html += "<input type='checkbox' checked name='"+ui.item.value+"' class='like-or-dislike' value='-1' />";
			html += "</td>";
			html += "<td class='col-md-1'><button type='button' class='close' onclick=\"$(this).parent().parent().remove(); return false;\">&times;</button></td>";
			html += "</tr>";
			$(this).parent().siblings("div").find("table > tbody").append(html).find(".like-or-dislike").likeOrDislike();
			return false;
		}
	});
	
	form.find("textarea[name='study_results']").val(data.results);
	
	// Patient Demographics
	if(data.patient_demographics) {
		form.find("select[name='gender']").val(data.patient_demographics.gender);
		form.find("textarea[name='inclusion_criteria']").val(data.patient_demographics.inclusion_criteria);
		form.find("input[name='minimum_age']").val(data.patient_demographics.minimum_age);
		form.find("input[name='maximum_age']").val(data.patient_demographics.maximum_age);
		form.find("input[name='count']").val(data.patient_demographics.count);
	}
	form.find("select[name='gender']").select2();
	
	// Marker Status
	var all_panels_div = form.find("div[data-name='all_panels']");
		
	for(var marker in data.marker_status) {
		var new_all_panels_div = all_panels_div.clone();
		new_all_panels_div.attr("data-name", "all_panels");
		new_all_panels_div.find("p[data-name='marker_gene_name']").html(marker);
		new_all_panels_div.find("input").each(function() {this.name += ":"+marker});
		new_all_panels_div.show();
		
		/*Mutation Panel*/
		all_panels_div.parent().append(new_all_panels_div);
	}
	
	form.find(".select-option-tooltip").tooltip({"placement":"right"});
}

/**
 * This function extracts the information from the pubmed form editing popup dialog and
 * sends it to the server.
 * @param form
 */
function submitCuratedForm(form) {
	form = $(form);
	var object = {"pmid":form.prop("id").substring(5)};
	
	try {
		var trial_info = form.find("select[name='trial_info']").val();
		var trial_ids = form.find("input[name='trial_ids']").select2("val");
		//var drug_names = $(form).find("input[name='drug_names']").val().split(",");
		var publication_types = $(form).find("select[name='publication_types']").val();
		var disease_annotations_manual = form.find("input[name='disease_annotations_manual']").select2("val");
		var disease_annotations_nlp = form.find("input[name='disease_annotations_nlp']").select2("val");
		var gender = form.find("select[name='gender']").val();
		var minimum_age = form.find("input[name='minimum_age']").val();
		var maximum_age = form.find("input[name='maximum_age']").val();
		var count = form.find("input[name='count']").val();
		var inclusion_criteria = form.find("textarea[name='inclusion_criteria']").val();
		var marker_statuses = {};
		
		form.find("div[data-name='all_panels']").each(function() {
			var gene_symbol = $(this).find("p[data-name='marker_gene_name']").html();
			var status = {"mutation" : {}, "gene_expression" : {}, "phosphorylation" : {}, "pathway" : {} };
			
			$(this).find("div[data-name='mutation_panel']").find("input:checked").each(function(){
				status["mutation"][this.name.split(":")[0]] = this.value;
			});
			
			$(this).find("div[data-name='ge_panel']").find("input:checked").each(function(){
				status["gene_expression"][this.name.split(":")[0]] = this.value;
			});
			
			$(this).find("div[data-name='phosphorylation_panel']").find("input:checked").each(function(){
				status["phosphorylation"][this.name.split(":")[0]] = this.value;
			});
			
			$(this).find("div[data-name='pathway_panel']").find("input:checked").each(function(){
				status["pathway"][this.name.split(":")[0]] = this.value;
			});
			
			marker_statuses[gene_symbol] = status;
		});
	} catch (err) {
		alert(err);
	}
	
	object["trial_info"] = trial_info;
	object["trial_ids"] = trial_ids;
	//object["drug_names"] = drug_names;
	object["publication_types"] = publication_types;
	object["disease_annotations_manual"] = disease_annotations_manual;
	object["disease_annotations_nlp"] = disease_annotations_nlp;
	object["gender"] = gender;
	object["marker_statuses"] = marker_statuses;
	
	var json = JSON.stringify(object);
	alert(json);
	console.log(form.find("input[name='disease_annotations_manual']").select2("html"));
	//$.ajax(base + "/pubmed/save_curated_publication?json_string="+json);
	
	return false;
}

/**
 * This function creates the filters for a given pubmed search
 * @param filter_key
 * @param filter_dom_element
 * @returns {___div1}
 */
function createActiveFilter(filter_key, filter_dom_element) {
	var form = document.forms['pubmed_search_form'];
	filter_value = $(filter_dom_element).html();
	
	var div = document.createElement("div");
	div.className = "label label-default";
	div.style.margin = "5px";
	div.innerHTML = filter_value + "&nbsp;";
	div.id = generateRandomString();
	div.style.display = "none";
	
	var span = document.createElement("span");
	span.className = "glyphicon glyphicon-remove clickSpan";
	div.appendChild(span);
	
	var input = document.createElement("input");
	input.setAttribute("type", "hidden");
	input.setAttribute("name", "filter");
	input.setAttribute("value", filter_key + ":" + filter_value);
	input.setAttribute("active-filter-id", div.id);
	
	document.getElementById("active-filters").appendChild(div);
	document.getElementById("filters").appendChild(input);
	
	$(div).click(function() {
		spinner.spin(document.getElementById("waiting"));
		var $this = $(this);
		$(form).find("input[active-filter-id='"+div.id+"']").remove();
		resetSearchForm(form);
		onSubmitSearch(function() {
			$this.remove();
			$(filter_dom_element).css("font-weight", "normal").css("text-decoration", "none").click(function () {
				$(this).filterTable(filter_key, $(this)); // Re-enable clicking for this filter
			});
		});
	});
	
	return div;
}

// Filter key e.g. "journal", Filter Value e.g. "Nature"
$.fn.filterTable = function(filter_key, filter_dom_element) {
	spinner.spin(document.getElementById("waiting"));
	var form = document.forms['pubmed_search_form'];
	var filter = createActiveFilter(filter_key, filter_dom_element);
	
	resetSearchForm(form);
	
	onSubmitSearch(function() {
		$(filter_dom_element).off("click").css("font-weight", "bold").css("text-decoration", "underline"); // Disable clicking for the same filter
		filter.style.display = "";
	});
}

function resetSearchForm(form) {
	$(form).find("input[name='get_filters']").val("no");	
	$(form).find("input[name='selected_pmids']").val("");
	$(form).find("input[name='pagenum']").val("1");
	$(form).find("input[name='move']").val("");	
	$(form).find("input[name='query_key']").val("");
}

function getTrialPhaseWithCounts(data) {
	var dict = {};
	for(var i = 0; i < data.length; i++) {
		if(dict[data[i]["journal_title"]]) dict[data[i]["journal_title"]] += 1;
		
		else dict[data[i]["journal_title"]] = 1;
	}
	return dict;	
}

$.fn.sortTable = function(sort_key) {
	var spinner = new Spinner().spin(document.getElementById("waiting"));
	var form = document.forms['pubmed_search_form'];
	$(form).find("input[name='pagenum']").val("1");
	$(form).find("input[name='sort_key']").val(sort_key);
	
	onSubmitSearch(function() {
		if(spinner) spinner.stop();
		$("#count-selected-pmids").html('0');
	});
	
	event.preventDefault();
}

/**
 * This creates an individual table row of Pubmed search results
 **/
function createSearchResultTableRow(row_data, row_num) {
	var html = "";
	var rowClass = "search-result-row-mouseout";
	if(selected_pmids.indexOf(row_data["pmid"]) > -1) rowClass = "search-result-row-select";
	if(reviewed_pmids.indexOf(row_data["pmid"]) > -1) rowClass += " reviewed"; // See if a given PMID has been visited before and if yes, mark it reviewed
	html += "<tr id='"+row_data["pmid"]+"'>"; // Setting Row ID to PMID
	html += "<td>" + (row_num) + "<br></td>";
	html += "<td class='"+rowClass+"' onmouseover='highlightRow(this)' onmouseout='unhighlightRow(this)' onclick='selectRow(this)'><div><span class='glyphicon glyphicon-play clickSpan link' data-pmid=\""+row_data["pmid"]+"\" onclick='getPublicationDetails(this)'></span> "+row_data["title"];
	html += "<br><b>Pubmed ID</b>: <i>"+row_data["pmid"]+"</i><br>";
	html += "<b>Journal</b>: <i>"+row_data["journal_title"]+"</i><br>";
	html += "<b>Date</b>: <i>"+row_data["date"]+"</i>";
	html += "<br>";
	//html += "<b>Clinical Trial</b>: ";
	for(var i = 0; i < row_data["trial_info"].length; i++) {
		html += "<span class='label label-clinical-trials'>"+row_data["trial_info"][i]+"</span>&nbsp;&nbsp;";
	}
	//html += "<br><br>";
	//html += "<b>Biomarkers</b>: ";
	if(row_data["biomarkers"])
		for(var i = 0; i < row_data["biomarkers"].length; i++){
			var annotation = row_data["biomarkers"][i];
			html += "<span class='label label-genes' data-toggle='tooltip' title='";
			html += annotation["original_text"]+"'>";
			html += annotation["normalized_text"]+"</span>&nbsp;&nbsp;";
		}
	
	if(row_data["diseases"])
		for(var i = 0; i < row_data["diseases"].length; i++) {
			var annotation = row_data["diseases"][i];
			html += "<span class='label label-diseases' data-toggle='tooltip' title='";
			html += annotation["original_text"]+"'>";
			html += annotation["normalized_text"]+"</span>&nbsp;&nbsp;";
		}
	
	html += "<br>";
	//html += "<div class='form-holder-div' style='display:none; overflow-x:auto'><div class='ui-widget'></div></div>"
	html += "</div></td>";
	html += "<td><input type='number' class='rating' min=0 max=5 step=1 data-size='sm'></td>";
	html += "</tr>";
	
	return html;
}

function highlightRow(col) {

	if($(col).hasClass("search-result-row-mouseout")) {
		$(col).addClass("search-result-row-mouseover");
		$(col).removeClass("search-result-row-mouseout");
	}
}

function unhighlightRow(col) {

	if($(col).hasClass("search-result-row-mouseover")) {
		$(col).addClass("search-result-row-mouseout");
		$(col).removeClass("search-result-row-mouseover");
	}
}

function selectRow(col) {
	
	if($(col).hasClass("search-result-row-mouseover")) {
		$(col).addClass("search-result-row-select");
		$(col).removeClass("search-result-row-mouseover");
		$(col).removeClass("search-result-row-mouseout");
		selected_pmids.push($(col).parent().attr("id"));
	}
	
	else {
		$(col).addClass("search-result-row-mouseover");
		$(col).removeClass("search-result-row-select");
		selected_pmids.splice(selected_pmids.indexOf($(col).parent().attr("id")), 1);
	}
	
	$("#count-selected-pmids").html(selected_pmids.length);
	if(selected_pmids.length > 0) {
		$("#page_count_and_number > div > div > button").removeClass("disabled");
	}
}