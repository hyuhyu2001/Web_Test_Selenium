var ui_function = function() {
};
// 沿用原js控件的名(这样能少改很多代码)
var ui = {
	_shadow : function() {
		return $("<div>").addClass("popup").addClass("boxShadow");
	},
	_box : function(type) {
		return $("<div>").addClass("popupContent").addClass("popBox").addClass("size").addClass("uisize").css({
			top : this._top(type)
		});
	},
	_title : function(title) {
		return $("<p>").addClass("popupTitle").addClass("uititleContent").append($("<span>").addClass("fl").html(title)).append(this._close());
	},
	_close : function() {
		return $("<a>").addClass("close").addClass("fr").attr("href", "javascript:void(0)").click(function() {
			ui._hide();
			ui_function(false);
		});
	},
	_text : function(type, text) {
		return $("<p>").addClass("right").append($("<input/>").addClass(type)).append($("<span>").html(text));
	},
	_enter : function(a) {
		var b = $("<a>").addClass("txtinfoBtn").attr("href", "javascript:void(0)").html("&#30830;&#35748;").click(function() {
			ui._hide();
			ui_function(true);
		});
		if ("confirm" == a || "alert" == a) {
			$(b).css({
				marginTop : 20
			})
		}
		return b;
	},
	_top : function(type) {
		var top = ($(window).height() - 200) / 2 + $(window).scrollTop();
		return top < 0 ? 0 : top;
	},
	_hide : function() {
		$($(".boxShadow")[$(".boxShadow").size() - 1]).remove();
		$($(".popBox")[$(".popBox").size() - 1]).remove();
	},
	popBox : function(text, type, titile) {
		$("body").append(this._shadow());
		var $div = this._box(type).append(this._title(titile)).append(this._text(type, text));
		$($div).append(this._enter(type));
		$("body").append($div);
		if ("confirm" != type) {
			ui_function = function() {
			};
		}
	},
	alert : function(text, func) {
		this.popBox(text, "alert", "&#20449;&#24687;&#25552;&#31034;");
		if (typeof func == "function") {
			$("div.popupContent a.txtinfoBtn").attr("onclick", "").click(function() {
				func();
			});
		}
	},
	success : function(text, func) {
		this.popBox(text, "success", "&#25104;&#21151;&#25552;&#31034;");
		if (typeof func == "function") {
			$("div.popupContent a.txtinfoBtn").attr("onclick", "").click(function() {
				func();
			});
		}
	},
	confirm : function(text, func) {
		this.popBox(text, "confirm", "&#30830;&#35748;&#26694;&#25552;&#31034;");
		if (typeof func != "undefined") {
			ui_function = func;
		}
	},
	error : function(text, func) {
		this.popBox(text, "error", "&#38169;&#35823;&#25552;&#31034;");
		if (typeof func == "function") {
			$("div.popupContent a.txtinfoBtn").attr("onclick", "").click(function() {
				func();
			});
			$(".uititleContent a.close").attr("onclick", "").click(function() {
				func();
			});
		}
	}
};