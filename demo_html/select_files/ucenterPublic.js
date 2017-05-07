function getSecondPermissionList(applyKey,tradingCenterKey,mode,obj){
	//用户类型获取
	var userType = $('#userType').val();
	if(userType == 2){
		jQuery(obj).siblings('ul').toggle();
		var i = $(obj).children()[0];
		if(i==undefined){
			$.ajax({
				url:'/ucenter/main/apply/CasGetSecondApplyListByApplication.do',
				type:'post',
				dataType : 'text',
				data:{
					'applyKey' : applyKey,
					'tradingCenterKey' : tradingCenterKey,
					'mode' : mode,
					'fid'  : '0'
				},
				success:function(result){
					if(result=="false"){
						window.location.reload();
					}else if(result==""){
						 $($(obj).children()[0]).remove();
						 $("#permissionContentForApply").css("top",(($(window).height() - 200) / 2 + $(window).scrollTop())+"px" );
						 $("#permissionNoticeForApply").show();	  		
					}else{
						$(obj).append('<i class="closeArrow"></i>') ;
						if(!result.startsWith("<li>")){ //防止返回登陆页
							window.location.reload();	
						}else{
							jQuery(obj).siblings('ul').html(result);
						}	
					}
				},
				error:function(){
					//validTip.wrong('网络异常，请重试');
					window.location.reload();
				}
			});
		}else{
			$(i).remove();
		}
	}else if(userType == 0){
		 $("#permissionContentForAuthen").css("top",(($(window).height() - 200) / 2 + $(window).scrollTop())+"px" );
		$("#permissionNoticeForAuthen").show();
	}	
}

function closeNoticeForAuthen(){
	  $("#permissionNoticeForAuthen").hide();
}

function closeNoticeForApply(){
	  $("#permissionNoticeForApply").hide();
}

function stringEmpty(str) {
	if (str != undefined) {
		if (str == null || this.trim(str).length == 0) return true;
		else return false;
	} else {
		return true;
	}
};

function StringBuffer() {
	
    this._strings_ = new Array();	
    this.append = function(str) {
	 this._strings_.push(str);
    }
    this.toString = function() {
	 return this._strings_.join('');
     }
}

function messageOut(obj) {
	$('#'+obj).hide(); 
	$('#'+obj).attr('lang',3);
}

/**
 * 绑定二级菜单鼠标滑入与滑出事件
 */
$(document).ready(function(){
	//左侧高度与右侧统一  --start
	//右侧主菜单高度
	var main_rHeight = $(".main_r").height();
	$('.main_l').css("min-height",(main_rHeight-3));
	//左侧高度与右侧统一  --end
	//首页微信弹出框  start
	var x=-50;
	var y=20;
	jQuery(".wechat").mouseover(function(e){
		var wx_content="<div class='big_box' style=\"z-index:999999999\">"+"<div class='wx_title'>"+"东煤交易官方微信"+"</div>"+"<div class='wx_ewm'>"+"<img src='/new2016/public/images/code_ecoal.gif' width='128' height='128'>"+"</div>"+"<div class='wx_bottom'>"+"打开微信，然后选择'扫一扫'，就可以了！欢迎关注东煤交易！"+"</div></div>";
		$(".box").append(wx_content);
		$(".big_box").css({left:(e.pageX+x)+'px',top:(e.pageY+y)+'px'}).show("fast");
	}).mouseout(function(){
		$(".big_box").remove();
	}).mousemove(function(e){
		$(".big_box").css({left:(e.pageX+x)+'px',top:(e.pageY+y)+'px'});
	});
	//首页微信弹出框  end
	
	//首页应用标签 绑定事件 start

	//首页应用标签 绑定事件 end
	
	//新版head 账户管理移入移出事件绑定  start
	$("#zhgl").live('mouseover',function(){
		$("#zhgls").parent().append("<span class='current'></span>");
		$("#zhgls").toggle(true);
	});
	$("#zhgl").live('mouseout',function(event){
		var obj = $(this).next().next().find('ul').find('a')[0];
		var eveObj =  $(event.relatedTarget)[0];
		var span = $("#zhgls").parent().find('span');
		if(event &&!$(obj).is($(eveObj))&&!$(eveObj).is(span)){
			$("#zhgls").parent().find("span").remove();
			$("#zhgls").toggle(false);
		}
	});
	$("#zhgls").live('mouseout',function(event){
		var lang = $($(this)[0]).children().first().children().first().attr('lang');
		if($(event.relatedTarget).attr('lang') != lang){
			$("#zhgls").parent().find("span").remove();
			$("#zhgls").toggle(false);
		}
	});
	
	
	$("#"+currentNavMenu).addClass("currentNavMenu");
	//新版head 账户管理移入移出事件绑定  end
	
	/*$("a[class='_second']").live('mouseover',function(){
			   var applyKey = $(this).parent().attr("applyKey");
				var tradingCenterKey = $(this).parent().attr("tradingCenterKey");
				var mode =  $(this).parent().attr("mode");
				var obj = $(this).parent();
				var fid = $(this).parent().attr("fid");
				getThirdPermissionList(applyKey,tradingCenterKey,mode,obj,fid);
				$(this).parent().find("ul").toggle(true);
	})
	$("a[class='_third']").live('mouseout',function(event){
		if($(event.relatedTarget).attr('lang') != $(this).attr('lang')){
			$(this).parents("ul.my_application_ul").toggle(false);
		}
	});
	$("a[class='_second']").live('mouseout',function(event){
		var obj = $(this).siblings("ul");
		if(event && !obj.find("a").is(event.relatedTarget)){
			obj.toggle(false);
		}
	});*/
})

/**
 * 获取三级菜单
 * @param {} applyKey
 * @param {} tradingCenterKey
 * @param {} mode
 * @param {} obj
 */
function getThirdPermissionList(applyKey,tradingCenterKey,mode,obj,fid){
	if($(obj).hasClass('s_tab_current')){
		$(obj).removeClass('s_tab_current');
	}else{
		$.ajax({
			url:$('#ctx').val()+'/main/apply/_CasGetThirdApplyListByApplication.do',
			type:'post',
			dataType : 'text',
			data:{
				'applyKey' : applyKey,
				'tradingCenterKey' : tradingCenterKey,
				'mode' : mode,
				'fid'  : fid
			},
			success:function(result){
				if(result=="false"){
					window.location.reload();
				}else{
					$(obj).find("ul").html(result);
				}
			},
			error:function(){
				validTip.wrong('网络异常，请重试');
			}
		});
	}
}

function getChildApplications(applyKey,tradingCenterKey,mode,menuId){
	$.ajax({
		url:$('#ctx').val()+'/main/apply/getApplyListByApplication.html',
		type:'post',
		dataType : 'text',
		data:{
			'applyKey' : applyKey,
			'tradingCenterKey' : tradingCenterKey,
			'mode' : mode,
			'fid'  : menuId
		},
		success:function(result){
			$('.my_application_ul').html('');
			$('#apply_'+menuId).prev('ul').html(result);
		},
		error:function(){
			validTip.wrong('网络异常，请重试');
		}
	});
}

/**
 * 发送手机验证码 冷却倒计时 提取公共方法
 * @param {} 
 * obj : 组件
 * 2014.08.26
 */
function phoneIntervalTime(obj){
	var intervalTime = $(obj).attr('lang');
	if(intervalTime == 'undefined' || !Boolean(intervalTime)){
		intervalTime = 60;
		$(obj).attr('lang',intervalTime);
	}
	$(obj).attr('km',1).html(intervalTime+'秒后重新发送');
	var interval = setInterval(function(){
		var time = $(obj).attr('lang');
		if(time == 1){
			$(obj).attr('km',2).html('获取验证码');
			clearInterval(interval);
			$(obj).attr('lang',intervalTime);
			$(obj).addClass("pointer");
		}else{
			$(obj).html(( time - 1)+'秒后重新发送').attr('lang',time - 1);
		}
	}, 1000);
}

/**
 * 密码校验
 * @param {} obj 密码
 * @param {} passId 二次密码
 * @return {Number}
 */
function checkStrong(obj,passId) {
    var sPW = $('#'+obj).val();
    var flag = false;
	if(sPW.length > 5){
		var regex = /^[a-zA-Z0-9_]{6,20}$/;
		if(regex.test(sPW)){
			$('#' + passId).removeAttr('disabled').removeClass('unclick');
			flag= true;
		}
	}
	if(!flag){
		$('#' + passId).val("").attr('disabled','disabled').addClass('unclick');
		validTip.normal($('#' + passId),"请再次输入密码，两次密码输入必须一致!");
		/*validTip.normal($("#confirm_password"),"请再次输入密码,两次密码输入必须一致!");*/
	}
    if (sPW.length < 1){
    	/*//$('.level_con').css('display', 'none');
    	$('#creatSafeCheck').css('display','none');*/
	    $('.level_con').css('display', 'none');
        return 0;
    }
    var Modes = 0;
    for (i = 0; i < sPW.length; i++) {
        Modes |= Evaluate(sPW.charCodeAt(i));
    }
    var chenum = bitTotal(Modes);
    if(sPW.length > 15){
    	chenum += chenum;
    }
    $("span.level_title").removeClass().addClass('level_title');
    if (chenum == 0) {
        return;
    } else if (chenum == 1) {
       $("span.level_title[lang='level_low']").addClass('font_red');
       $("span.level_line").removeClass('high').removeClass('senior').addClass('low').attr('title','安全等级：低');
    } else if (chenum == 2) {
        $("span.level_title[lang='level_senior']").addClass('font_yellow');
        $("span.level_line").removeClass('high').removeClass('low').addClass('senior').attr('title','安全等级：中');
    } else if (chenum >= 3) {
    	$("span.level_title[lang='level_high']").addClass('font_green');
    	$("span.level_line").removeClass('senior').removeClass('low').addClass('high').attr('title','安全等级：高');
    }
    $('.level_con').css('display', '');
}

function Evaluate(character) {
    if (character >= 48 && character <= 57)
        return 1;
    if (character >= 65 && character <= 90)
        return 2;
    if (character >= 97 && character <= 122)
        return 4;
    if (character == 95)
        return 8;
    else
        return 0;    
}

function bitTotal(num) {
    var modes = 0;
    for (i = 0; i < 4; i++) {
        if (num & 1) modes++;
        num >>>= 1;
    }
    return modes;
}

function applyContent(){
	window.location.href = "/";
}

/**
 * 账号密码校验 是否重合
 * @param {} config
 * @param {} s1 账号
 * @param {} s2 密码
 * @return {Boolean}
 */
function passwordAndNameCheck(config,s1,s2){
	var limit = /^[a-zA-Z0-9_]{6,20}$/;
	if(!s2.val()){
		validTip.normal(s2,config.empty);
		return false; //返回假，以供最后验证
	}
	if(s1.val() == s2.val()){
		validTip.wrong(s2,"您的密码与账户信息太重合，有被盗风险，请换一个密码");
		return false; //返回假，以供最后验证
	}
	if(limit.test(s2.val())){
		validTip.right(s2,config.right);
		return true; //返回傎，以供最后验证
	}else{
		validTip.wrong(s2,config.wrong);
		return false; //返回假，以供最后验证
	}
}

function password_repeat(config,s1,s2){
	if($.trim(s1.val()).length == 0){
		validTip.wrong(s1,config.empty);
		return false;
	}
	if($.trim(s1.val()) == $.trim(s2.val())){
		validTip.right(s1,config.right);
		return true; //返回傎，以供最后验证
	}else{
		validTip.wrong(s1,config.wrong);
		return false; //返回假，以供最后验证
	}
}
/**
 * 获取服务管理二级菜单
 */
function getFwglSecondList(){
	var obj = $("#fwglMenu");
	var objl = $("#fwglMenu a");
	var obja = $("#fwglA");
	var flag = obj.attr("expand");
	if(flag=="true"){
		//$("#fwglMenu li").hide();
		obj.attr("style","display:block");
		obja.attr("class","s_tab_current");
		objl.attr("class","");
		obj.attr("expand",false);
	}else{
			//$("#fwglMenu li").show();
			obj.attr("style","display:none");
			obja.attr("class","");
			obj.attr("expand",true);
	}

}
//	用户退出操作
function loginout(){
	$.ajax({
		type:'post',
		url:$('#ctx').val()+'/main/userLogin/_CasCheckLogin.do',
		dataType:'json', 
		success:function(doc,flag,ret){
			var ret = ret.responseText;
			if(ret=="true"){
				var casUrl = $("#mycasUrl").val();
				var basePath = $("#basePath").val();
				window.location.href=casUrl+"/remoteLogout?service=http://"+basePath+"/main/userLogin/toLogin.html";
			}else{
				window.location.reload();
			}
		}
		})
}


//打开东煤协议
function openProtocol(){
	//$("#protocolsize").css("top",(($(window).height() - 0) / 2 + $(window).scrollTop())+"px" );
	$("#protocolAgreement").animate({scrollTop:0},1);
	$("#protocol").show();
}

//关闭东煤协议
function closeProtocol(){
	 $("#protocol").hide();
}

//一级菜单二级菜单定位  firstPermissionName 一级菜单名称（例如'团购'）  secondPermissionName 二级菜单名称(例如'发团管理')
function permissionSelect(firstPermissionName,secondPermissionName){
	  for(var i=0;i<$(".subNav").length;i++){
		    var firstJqObj = $($(".subNav")[i]);
			  if (firstJqObj.text() == firstPermissionName || firstJqObj.text() == firstPermissionName+"<i class='closeArrow'></i>"){
			  	  $(firstJqObj).click();
			  	  firstJqObj.html(firstPermissionName+"<i class='closeArrow'></i>");
			  	  var  ulJqObj = $(firstJqObj.next(".navContent"));
			  	  for(var j=0;j<ulJqObj.find("li").length;j++){
			  		   var secondJqObj = $(ulJqObj.find("li").eq(j));	  
		  		       if (secondJqObj.find("a").text() == secondPermissionName ||secondJqObj.find("a").text() == "<i></i>"+secondPermissionName){
			  		       secondJqObj.addClass("currentItem");
			  		       break;
		  		       }
			  	  }
			  }
	    }
}

/**
 * 定时关闭窗口js
 * @param {} winId
 */
function closeWindow(winId){
	var interval = setInterval(function(){
		var time = $('#'+winId).attr('lang');
		if(time == 1){
			 clearInterval(interval);
			 $('#'+winId).hide();
			 $('#'+winId).attr('lang',3);
		}else{
			$('#'+winId).attr('lang',time - 1);
		}
	},1000);
}

String.prototype.endsWith=function(s){
  if(s==null||s==""||this.length==0||s.length>this.length)
     return false;
  if(this.substring(this.length-s.length)==s)
     return true;
  else
     return false;
  return true;
 }
 String.prototype.startsWith=function(s){
  if(s==null||s==""||this.length==0||s.length>this.length)
     return false;
  if(this.substr(0,s.length)==s)
     return true;
  else
     return false;
  return true;
 }
 
 //企业审核通过后默认展开团购
 function getTgPermissionList(applyKey,tradingCenterKey,mode,obj){
 		//默认展开东煤城市商城
 		applyKey = '1008';
		//用户类型获取
		var userType = $('#userType').val();
		if(userType == 2){
			obj.siblings('ul').toggle();
			var i = obj.children()[0];
			if(i==undefined){
				$.ajax({
					url:'/ucenter/main/apply/CasGetSecondApplyListByApplication.do',
					type:'post',
					dataType : 'text',
					data:{
						'applyKey' : applyKey,
						'tradingCenterKey' : tradingCenterKey,
						'mode' : mode,
						'fid'  : '0'
					},
					success:function(result){
						if(result=="false"){
							window.location.reload();
						}else if(result==""){
							 $(obj.children()[0]).remove();
						}else{
							obj.append('<i class="closeArrow"></i>') ;
							if(!result.startsWith("<li>")){ //防止返回登陆页
								window.location.reload();	
							}else{
								obj.siblings('ul').html(result);
							}	
						}
					},
					error:function(){
						//validTip.wrong('网络异常，请重试');
						window.location.reload();
					}
				});
			}else{
				$(i).remove();
			}
		}
	}

 
 
 var app_arr = [ [ "东煤城市商城", "/mallweb/" ], [ "撮合", "/dcx/" ]];

 function setAppSelect() {
 	
 	if(-1 == location.href.indexOf("/ucenter/main/")){
 		//$(getAppNodeByAppName(app_arr[0][0])).click();// 东煤商城展开
 		getTgPermissionList('1008','25fd877ed7eb1e82979043cc6d4f5bf5','003',$("#dmscSubNav"));
 	}
 	for (var i = 1; i < app_arr.length; i++) {// 对应其他项目展开
 		if (-1 != location.href.indexOf(app_arr[i][1])) {
 			$(getAppNodeByAppName(app_arr[i][0])).click();
 		}
 	}
 }
 function getAppNodeByAppName(appName) {
 	var node = null;
 	$(".subNavBox div a.subNav").each(function(i, a) {
 		if ($(a).html() == appName) {
 			node = a;
 		}
 	});
 	return node;
 }

 $(document).ajaxComplete(function() {
 	var z = new Array();
 	var url = typeof _childHref != "undefined" ? _childHref : location.href.substring(location.href.indexOf("/",7));
 	$("ul.navContent li").each(function(i, l) {
 		if ($(this).children("a").attr("href").indexOf(url) != -1) {
 			$(this).removeClass("currentItem");
 			z.push($(this));
 		}
 	});
 	$(z[z.length-1]).addClass("currentItem");
 	var _menu_name_ = null;
 	var _menu_name_value_ = null;
 	if(url.indexOf('/dcx/') > -1 && url.indexOf('jump') > -1){
 		   _menu_name_value_ = getQueryString('jump');
 		if('sellAnnouncement' == _menu_name_value_){
 			_menu_name_ = '发售查询';
 		}else{
 			_menu_name_ = '申购查询';
 		}
 	}else if(url.indexOf('/mallweb/') > -1 && url.indexOf('sellOrBuy') > -1){
 		_menu_name_value_ = getQueryString('sellOrBuy');
 		if('sell' == _menu_name_value_){
 			_menu_name_ = '销售订单管理';
 		}else{
 			_menu_name_ = '采购订单管理';
 		}
 	}
 	if(_menu_name_){
 		try{
 			$('ul.navContent').find("a[title='"+_menu_name_+"']").parent().addClass('currentItem');
 		}catch(e){}
 	}
 });
 $(function() {
 	setAppSelect();// 展开对应项目
 });
 //获取路径中的指定参数
 function getQueryString(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)","i");
	var r = window.location.search.substr(1).match(reg);
	if (r!=null) return (r[2]); return null;
}