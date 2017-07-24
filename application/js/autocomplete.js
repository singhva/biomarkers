	function split( val ) {
	     return val.split( /\s+/ );
	}

$( "#term2" )
  // don't navigate away from the field on tab when selecting an item
  .bind( "keydown", function( event ) {
    if (event.keyCode === $.ui.keyCode.TAB) {
      	event.preventDefault();
    }
    
    else if (event.keyCode === $.ui.keyCode.BACKSPACE) {
    	var length = $(this).contents().length;
    	var contents = $(this).contents();
    	console.log(contents[length - 1].nodeType);
    	var nodeName = contents[length - 1].nodeName;
    	if (nodeName == "BR") {
    		$(contents[length - 1]).remove();	        		
    	}
    	
    	else if (nodeName == "#text") {
    		if($(contents[length - 1]).text() == String.fromCharCode(160)) {
    			$(contents[length - 1]).remove();
    			length = $(this).contents().length;
    			$(contents[length - 1]).remove();
    			$(this).append("&nbsp;&nbsp;");
    			console.log("1");
    		}
    	}
    	
    	if (length >= 2) $(contents[length - 2]).remove();
    	$(this).append("&nbsp;&nbsp;");
    	/*
    	if(contents[length - 1].nodeType == 3) {
    		if($(contents[length - 1]).text() == String.fromCharCode(160)) {
    			$(contents[length - 1]).remove();
    			length = $(this).contents().length;
    			$(contents[length - 1]).remove();
    			$(this).append("&nbsp;&nbsp;");
    			console.log("1");
    		}
    	}	        	
    	else {
    		$(contents[length - 1]).remove();
    		$(contents[length - 2]).remove();
    		$(this).append("&nbsp;&nbsp;");
    		console.log("2");
    	}
    */
    	placeCaretAtEnd(this);
    }
    
    else if (event.keyCode === $.ui.keyCode.SPACE) {	        	 
    	var length = $(this).contents().length;
    	var contents = $(this).contents();
    	if(contents[length - 1].nodeName == "BR") {
    		$(contents[length - 1]).remove();
    		length--;
    	}
    	if( (contents[length - 1].nodeType == 3) ) {
    		var text = $(contents[length - 1]).text().trim();
    		if((text != String.fromCharCode(160)) || (text.trim() != "")) {
    			var text = $(contents[length - 1]).text().replace(/\s*/g, "");
    			$(contents[length - 1]).remove();
    			$(this).append("<span class='rounded-corner-label'>"+text+"</span>&nbsp;");
    			//placeCaretAtEnd(this);	        			
    		}
    		
    		else {
    			contents.last().remove();
    			$(this).append("&nbsp;");
    			//placeCaretAtEnd(this);
    		}
    	}
    	// Merge last two spans if they both contain free text
    	var spans = $(this).find("span");
    	var last = $(spans[spans.length - 1]);
    	var second_to_last = $(spans[spans.length - 2]);
    	if ( (last.attr("class") == second_to_last.attr("class")) && (last.attr("class") == "rounded-corner-label") ) {       		
    		second_to_last.html(second_to_last.html().trim() + " " + last.html().trim());
    		last.remove();
    	}
    	placeCaretAtEnd(this);
    	$(this).autocomplete('close');
    }
  }).click(function(event) {
	  placeCaretAtEnd(this);
	  event.preventDefault();
  })
  .autocomplete({
    minLength: 3,
    delay: 0,
    autoFocus: true,
    source: function( request, response ) {
      // delegate back to autocomplete, but extract the last term
      query = split( request.term ).pop();
      if(query.length > 2)
      $.getJSON( base + "/lookups/autocomplete_gene_symbol", {
            term: query
          }, response );
      
      /*
    	response( $.ui.autocomplete.filter(
                availableTags, extractLast( request.term ) ) );
      */
    },
    select: function( event, ui ) {
    	console.log("inside select");
    	var contents = $(this).contents();
    	var length = contents.length;
    	//console.log("last nodename: "+contents[length - 1].nodeName);
    	if(contents[length - 1].nodeName == "BR") {
    		$(contents[length - 1]).remove();
    		length--;
    	}
    	contents[length - 1].remove();
    	var val = ui.item.value;
    	console.log($(val).html());				
		
		$(this).append("<div class='rounded-corner-label label-genes'>"+$(val).html()+"<span class='glyphicon glyphicon-remove'></span></div>");
		$(this).append("&nbsp;");
		event.preventDefault();
		placeCaretAtEnd(this);
		this.focus();
		return false;
    }
  }).focus().data("ui-autocomplete")._renderItem = function(ul, item) {
		var span = $(item.value);
		var li = document.createElement("li");
		var a = document.createElement("a");
		a.innerHTML = span.html()
		var span1 = document.createElement("span");
		span1.className = span.attr("class");
		span1.innerHTML = "G";
		span1.style.cssFloat = "right";
		return $(li).append($(a).append(span1)).appendTo(ul);
		//return $("<li><a>"+span.html()+"<span style='float: right;' class='"+span.attr("class")+"'>G</span></a></li>").appendTo(ul);
	  };
