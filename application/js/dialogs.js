function createDialogs() {
	// Popup form editing dialog
	$("#form-holder-div").dialog({
	      height: 600,
	      width: 1000,
	      modal: true,
	      autoOpen: false,
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
	                {text: 'Save', class: 'btn btn-primary', click: function() {submitCuratedForm($(this).find(".ui-widget > form"))}},
	                {text: "Cancel", class:"btn btn-danger", click: function() { 
		                	$(this).dialog("close"); 
		                	$(this).find(".ui-widget > form").remove();
		                	$(this).find(".ui-widget > form > .select2").select2('destroy');
		                	$(".select2-hidden-accessible").remove();
	                	}
	                }
	      ]
	});
	
	// Mutation name dialog
	$("#enter-mutation-name-dialog").dialog({
	      height: 300,
	      modal: true,
	      autoOpen: false,
	      buttons: [
	         {
	        	 text: "Ok", class:"btn btn-primary", click:function() {
	        		$(element).html($(this).find("input").val());
		      		$(this).find("input").val("");
		      		$(this).dialog("close");		        		 
	        	 }
	         },
	         {
	        	 text: "Cancel", class:"btn btn-danger", click: function() { $(this).find("input").val(""); $(this).dialog("close"); }
	         }
	      ]
	});
	
	// Pathway name dialog
	$("#enter-pathway-name-dialog").dialog({
	      height: 300,
	      modal: true,
	      autoOpen: false,
	      buttons: [
	         {
	        	 text: "Ok", class:"btn btn-primary", click:function() {
	        		$(element).html($(this).find("input").val());
		      		$(this).find("input").val("");
		      		$(this).dialog("close");		        		 
	        	 }
	         },
	         {
	        	 text: "Cancel", class:"btn btn-danger", click: function() { $(this).find("input").val(""); $(this).dialog("close"); }
	         }
	      ]
	});
	
	$("#enter-disease-name-dialog").dialog({
	      height: 300,
	      modal: true,
	      autoOpen: false,
	      create: function(event, ui) {
	    	 var $this = $(this);
	  		 $(this).find("input").autocomplete({
				source: base + "/lookups/autocomplete_disease_name",
				minLength: 3,
				delay: 500,
				select: function(event, ui) {
					$this.find("i").html(ui.item.label);
					$this.find("input[type='hidden']").val(ui.item.value);
					event.preventDefault();
				}
			});
	      },
	      open: function(event, ui) {
	    	var a = $(this).find("a");
	    	var trigger = $(this).data("trigger");
    		a.html(trigger.innerHTML);
    		$(this).dialog('option', 'position', {my: 'left top', of: trigger});
	      },
	      buttons: [
	         {
	        	 text: "Ok", class:"btn btn-primary", click:function() {
	        		var $this = $(this);
	        		var trigger = $(this).data("trigger");
	        		//var range = $("#read-abstract-dialog").data("range"); // Range is a dictionary, not the Javascript Range object
	        		var pmid = $("#read-abstract-dialog").attr("data-pmid"); // Could be potentially stored in "trigger"
	        		var annotation = $(this).find("input[type='hidden']").val();    
	        		var startOffset = $(trigger).attr("startOffset");
	        		var endOffset = $(trigger).attr("endOffset");
	        		var data = "pmid="+pmid+"&original_text="+trigger.innerHTML+"&db_id="+annotation + 
	        					"&start_pos="+startOffset+"&end_pos="+endOffset;					
	        		$.ajax(base + "/pubmed/save_disease_annotation", {data: data,
	        			success: function() {
	        				trigger.className = "highlight";
	        				$this.dialog("close");
	        				/*if(range.endOffset > range.startOffset) {
	        					var newRange = document.createRange();
	        					var startNode = document.getElementById("read-abstract-dialog").getElementsByTagName("p");
	        					var textNode = startNode.item(0).firstChild; // This is the text node of the abstract      
	        					newRange.setStart(textNode, range.startOffset);
	        					newRange.setEnd(textNode, range.endOffset);
	        					var span = document.createElement('span');
	        				    span.className = 'highlight';	        					
	        					span.ondblclick = function() {
	        						$this.dialog("open");
	        					};
	        					span.onclick = function() {
	        						return false;
	        					}
	        					newRange.surroundContents(span);
	        				}*/
	        			},
	        			error: function() {
	        				var trigger = $(this).data("trigger");
	        				var parent = trigger.parentNode;
	        				var textnode = document.createTextNode(trigger.innerHTML);
	        				parent.insertBefore(textnode, trigger);
	        				parent.removeChild(span);
	        			}
	        		});		      		
	        	 }
	         },
	         {
	        	 text: "Cancel", class:"btn btn-danger", click: function() {
     				var trigger = $(this).data("trigger");
     				var sibling = trigger.nextSibling;
     				var parent = trigger.parentNode;
	    			sibling.insertData(0, trigger.innerHTML);
	    			parent.removeChild(trigger);
	        		$(this).dialog("close");
	        	 }
	         }
	      ]
	});
	
	// Drug name dialog
	$("#enter-drug-name-dialog").dialog({
	      height: 300,
	      modal: true,
	      autoOpen: false,
	      buttons: [
	         {
	        	 text: "Ok", class:"btn btn-primary", click:function() {
	        		//$(element).siblings().html($(this).find("input").val());
	    			html += "<tr class='col-md-8'>";
	    			html += "<td class='col-md-6'>"+data.drugs[drug_id]+"</td>";
	    			html += "<td class='col-md-2'>";
	    			html += "<input type='checkbox' checked name='"+drug_id+"' class='like-or-dislike' value='-1' />";
	    			html += "</td>";
	    			html += "</tr>";
		      		$(this).find("input").val("");
		      		$(this).dialog("close");		        		 
	        	 }
	         },
	         {
	        	 text: "Cancel", class:"btn btn-danger", click: function() { $(this).find("input").val(""); $(this).dialog("close"); }
	         }
	      ]
	});
	
	// Advanced options dialog
	$("#show-advanced-options").dialog({
		minWidth: "500", 
		maxHeight: "300", 
		height: "300", 
		width: "500",
		autoOpen: false,
		appendTo: "#pubmed_search_form",
		modal: true,
		open: function(event, ui) {
	        $(this).find("input").blur();
	    },
		buttons:[
			{text: "Close", class:"btn btn-danger", click: function() {$( this ).dialog( "close" )}}
		]
	});
	
	// Read abstract dialog
	$("#read-abstract-dialog").dialog({
		minWidth: "500", 
		maxHeight: "300", 
		height: "300", 
		width: "500",
		autoOpen: false,
		open: function(event, ui) {
	        $(this).dialog('widget').find("button").blur();
	        $(this).dialog('option', 'title', $(this).attr('title'));
		},
	    create: function(event, ui) {
	    	var $this = $(this);
			$(this).find('p').mouseup(function() {
				var selected;
				var text = "";
			    if (window.getSelection) {
			        selected = window.getSelection();
			        text = selected.toString();
			    } else if (document.selection) {
			        selected = document.selection.createRange();
			        text = selected.text;
			    }
			    var range = selected.getRangeAt(0);
			    var startOffset = range.startOffset;
			    var endOffset = range.endOffset;
				console.log("selected: "+text+", startoffset: "+
						startOffset+", endoffset: "+endOffset+", range: "+range.toString());
				//$this.data("range", { "text" : text, "startOffset" : startOffset, "endOffset" : endOffset });
				if (endOffset > startOffset) { // Ensures that we don't open the autocomplete dialog by an accidental click
					var span = document.createElement('span');
				    span.className = 'highlight-temp';
				    span.setAttribute("startOffset", startOffset);
				    span.setAttribute("endOffset", endOffset);
					span.ondblclick = function() {
						$("#enter-disease-name-dialog").data("trigger", span);
						$("#enter-disease-name-dialog").dialog('open');
					};
					//newRange.surroundContents(span);		
					range.surroundContents(span);
					$(span).trigger("dblclick");
				}				
			});		    	
	    },
		buttons:[{text:"Close", class:"btn btn-primary", click: function() {$( this ).dialog( "close" );}}]
	});


}


function enterMutationName(element) {
	$("#enter-mutation-name-dialog").dialog("open");
}

function enterPathwayName(element) {
	$("#enter-pathway-name-dialog").dialog("open");
}

function enterDrugName(element) {
	$("#enter-drug-name-dialog").dialog("open");
}

function getSelectedRange() {
	var selected;
	var text = "";
    if (window.getSelection) {
        selected = window.getSelection();
        text = selected.toString();
    } else if (document.selection) {
        selected = document.selection.createRange();
        text = selected.text;
    }
    return selected.getRangeAt(0);
}

function createAnnotatedText(startOffset, endOffset, textNode, ondblclick) {
	if(endOffset > startOffset) {
		var newRange = document.createRange();
		//var startNode = document.getElementById("read-abstract-dialog").getElementsByTagName("p");
		//var textNode = startNode.item(0).firstChild; // This is the text node of the abstract      
		newRange.setStart(textNode, startOffset);
		newRange.setEnd(textNode, endOffset);
		var span = document.createElement('span');
	    span.className = 'highlight';	        					
		span.ondblclick = ondblclick;
		newRange.surroundContents(span);
	}
}
