$.fn.plusMinusToggle = function(toggledElement) { //toggledElement is a DOM element or jQuery object
	var self = $(this);
	var plusMinus = jQuery(document.createElement("span"));
	plusMinus.html("[+]&nbsp;");
	var element = jQuery(toggledElement);
	var text = self.html();
	self.prepend(plusMinus);
	element.hide();
	
	var toggleFunction = function() {
		if(plusMinus.html().indexOf("+") > -1) {
			element.show();
			var replaceValue = plusMinus.html().replace("+","-");
			plusMinus.html(replaceValue);
		}
		
		else if(plusMinus.html().indexOf("-") > -1){
			element.hide();
			var replaceValue = plusMinus.html().replace("-","+");
			plusMinus.html(replaceValue);
		}
	};
	self.click(toggleFunction);		
	
	return self;
};

$.fn.showOrHide = function(form) {
	var self = $(this);
	self.parent().sticky_div();
	self.siblings(".pull-right").show();
	self.parent().find("input[type=submit]").click(function(){submitCuratedForm(form)});
	var div = document.createElement("div");
	div.className = "rounded-corner";					
	self.parents("li").append(div);
	self.removeAttr("onclick");
	$(div).html(form);
	self.click(function() {
		var triangle = $(this).find('span');
		//var sticky = $(this).parent();
		$(this).parents("li").siblings(".last-reviewed").attr("class","reviewed");
		$(this).parents("li").attr("class","last-reviewed");
		
		if(triangle.hasClass("ui-icon-triangle-1-e")) {
			$(triangle).removeClass("ui-icon-triangle-1-e");
			$(triangle).addClass("ui-icon-triangle-1-s");
			//$(this).siblings(".pull-right").show();
			//$(this).attr("data-window-position", $(window).scrollTop());
		}
		
		else {
			$(triangle).removeClass("ui-icon-triangle-1-s");
			$(triangle).addClass("ui-icon-triangle-1-e");
			//sticky.find(".pull-right").hide();
			//$(window).scrollTop($(this).attr("data-window-position"));
		}
		//sticky.siblings('div').toggle();
	});
	
	var triangle = self.find('span');
	$(triangle).removeClass("ui-icon-triangle-1-e");
	$(triangle).addClass("ui-icon-triangle-1-s");
	//self.attr("data-window-position", $(window).scrollTop());
	$(this).parents("li").siblings(".last-reviewed").attr("class","reviewed");
	$(this).parents("li").attr("class","last-reviewed");
};

$.fn.toggleBetweenClasses = function(class1, class2) {
	var self = $(this);
	if(self.hasClass(class1)){
		self.removeClass(class1);
		self.addClass(class2);
	}
	
	else if(self.hasClass(class2)) {
		self.removeClass(class2);
		self.addClass(class1);
	}
	
};

$.fn.likeOrDislike = function(options) {
	var self = $(this);
	var defaultOptions = {};
	
	if(typeof(options) == "object" || typeof(options) == "undefined") {
		$.extend(defaultOptions, options);
		var div = document.createElement("div");
		var like = document.createElement("span");
		var dislike = document.createElement("span");
		div.className = "thumbs-parent";
		like.className = "glyphicon glyphicon-thumbs-up clickSpan glyphicon-inactive";
		dislike.className = "glyphicon glyphicon-thumbs-down clickSpan glyphicon-inactive";
		
		$(div).click(function(event) {
			var target = event.target;
			var sibling = $(target).siblings("span");
			
			if($(target).hasClass("glyphicon-inactive")) {
				$(target).removeClass("glyphicon-inactive").addClass("thumbs-active");
			}
			
			else {
				$(target).addClass("glyphicon-inactive").removeClass("thumbs-active");
			}
			
			if(!sibling.hasClass("glyphicon-inactive")) {
				sibling.addClass("glyphicon-inactive").removeClass("thumbs-active");
			}
		});
		
		div.appendChild(like);
		div.appendChild(dislike);
		self.parent().append(div);
		self.hide();
		self.removeClass("like-or-dislike");
	}
	
	else if(options === "val"){		 
		var active = $(this).siblings("div.thumbs-parent").find("span.thumbs-active");
		if(active.hasClass("glyphicon-thumbs-up")) return 1;
		
		else if(active.hasClass("glyphicon-thumbs-down")) return 0;
		
		else return -1;		
	}
}

function updateGlobalAlert(message, type, timeout) {
	var alert_div = $("#results-alert");
	var defaultTimeout = 3000;
	
	if(type == "warning") alert_div.attr("class", "alert alert-warning").html(message);
	
	else if(type == "error") alert_info.attr("class", "alert alert-danger").html(message);
	
	else alert_div.attr("class", "alert alert-info").html(message);
	
	if (timeout == 0) {
		alert_div.fadeIn();
	}
	
	else {
		alert_div.fadeIn().delay(timeout? timeout:defaultTimeout).fadeOut();
	}
	
}

function generateRandomString() {
	return Math.random().toString(36).substring(2, 7);
}

function placeCaretAtEnd(el) {
    el.focus();
    if (typeof window.getSelection != "undefined"
            && typeof document.createRange != "undefined") {
        var range = document.createRange();
        range.selectNodeContents(el);
        range.collapse(false);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
    } else if (typeof document.body.createTextRange != "undefined") {
        var textRange = document.body.createTextRange();
        textRange.moveToElementText(el);
        textRange.collapse(false);
        textRange.select();
    }
}