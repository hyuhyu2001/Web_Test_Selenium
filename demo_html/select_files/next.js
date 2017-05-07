function bindcheck(lis){
	$.each(lis,function(i,n){
		if(n==0){
			check_blur('companyName',$('#companyName'),false,false);
		}else if(n==1){
			check_blur('userName',$('#userName'),true,false);
		}else if(n==2){
			check_blur('companyType',$('#companyType_value'),true,true);
		}else if(n==3){
			check_blur('profession',$('#profession_value'),true,true);
		}else if(n==4){
			check_blur('province',$('#province'),true,true);
		}else if(n==5){
			check_blur('city',$('#city'),true,true);
		}else if(n==6){
			check_blur('area',$('#area'),true,false);
		}else if(n==7){
			check_blur('companyTypeText',$('#companyTypeText'),true,true);
		}else if(n==8){
			check_blur('professionText',$('#professionText'),true,true);
		}
	});
}
function subcheck(lis){
	var blbl = true,alal=true;
	$.each(lis,function(i,n){
		if(n==0){
			alal = check_single('companyName',$('#companyName'),false,false);
		}else if(n==1){
			alal = check_single('userName',$('#userName'),true,false);
		}else if(n==2){
			alal = check_single('companyType',$('#companyType_value'),true,true);
		}else if(n==3){
			alal = check_single('profession',$('#profession_value'),true,true);
		}else if(n==4){
			alal = check_single('province',$('#province'),true,true);
		}else if(n==5){
			alal = check_single('city',$('#city'),true,true);
		}else if(n==6){
			alal = check_single('area',$('#area'),true,false);
		}else if(n==7){
			alal = check_single('companyTypeText',$('#companyTypeText'),true,true);
		}else if(n==8){
			alal = check_single('professionText',$('#professionText'),true,true);
		}
		!alal?blbl=alal:'';
	});
	return blbl;
}
function subTextcheck(){
	var blbl = true,alal=true;
	if("其他"==$.trim($('#companyType_value').val())){
		alal = check_single('companyTypeText',$('#companyTypeText'),true,true);
	}
	if("其他"==$.trim($('#profession_value').val())){
		blbl = check_single('professionText',$('#professionText'),true,true);
	}
	return alal&&blbl;
}
;(function(){
	window.my_mess={
		companyName:['请输入企业全称'
		         ,"企业名称不能为空"
		         ,/[^\s]{1,}/
		         ,"企业名称不合法"
		         ,'该企业名称已经存在'
		         ,"comNameIsAt.html"
		         ],
		userName:["请输入姓名"
		       ,"姓名不能为空"
		       ,/^([\u4E00-\u9FA5]+|[a-zA-Z]+)$/
		       ,"您输入的姓名不合法"	 
		       ],
		companyType:['请选择企业类型'
		      ,'企业类型不能为空'
		      ],
		profession:['请选择所属行业'
              ,'所属行业不能为空'
              ],
        area:['请选择所在省市'
              ,'省市不能为空'
              ],
        province:['请选择所在省'
                  ,'省市不能为空'
              ],
        city:['请选择所在市'
              ,'省市不能为空'
              ],
        companyTypeText:['请输入企业类型'
                         ,'请输入企业类型'
                         ],
        professionText:['请输入所属行业'
                        ,'请输入所属行业'
                        ],
		common:['网络异常，请重试']
	
	};
})();
function mess(m,n){
	if(m==='companyName'){
		return my_mess.companyName[n];
	}
	if(m==='userName'){
		return my_mess.userName[n];
	}
	if(m==='companyType'){
		return my_mess.companyType[n];
	}
	if(m==='profession'){
		return my_mess.profession[n];
	}
	if(m==='province'){
		return my_mess.province[n];
	}
	if(m==='city'){
		return my_mess.city[n];
	}
	if(m==='area'){
		return my_mess.area[n];
	}
	if(m==='companyTypeText'){
		return my_mess.companyTypeText[n];
	}
	if(m==='professionText'){
		return my_mess.professionText[n];
	}
	if(m==null){
		return my_mess.common[n];
	}
};
window.validTip={
	right:function(obj,text){
		$(obj).parent().find(".hint").addClass('noVisible');
	},
	wrong:function(obj,text){
		$(obj).parent().find(".hint").removeClass('noVisible').html(text);
	},
	normal:function(obj,text){
		$(obj).parent().find(".hint").addClass('noVisible');
	},
	clear:function(obj,text){
		$(obj).parent().find(".hint").addClass('noVisible');
	}
};
function bnu(o){
	return o==null||o==''||o==undefined;
}
function check_pass(lg,obj,bl){
	var _obj = $(obj),sv = $.trim(_obj.val()),regx = mess(lg,2);
	if(bnu(sv)){
		validTip.wrong(_obj,mess(lg,1));
		return false;
	}else if(!regx.test(sv)){
		validTip.wrong(_obj,mess(lg,3));
		return false;
	}else if(bl){

	}
}
function check_blur(lg,obj,bl,al){
	$(obj).focus(function(){
		validTip.wrong($(this),mess(lg,0));
		return false;
	}).blur(function(){
		return check_single(lg,$(this),bl,al);
	});
}
function check_select(m,n){
	if(m==='companyType'||m==='companyTypeText'){
		right_wrong($("#dnw1"),mess(m,1),n);
	}
	if(m==='profession'||m==='professionText'){
		right_wrong($("#dnw2"),mess(m,1),n);
	}
	if(m==='province'||m==='city'){
		right_wrong($("#dnw3"),mess(m,1),n);
	}

}
function right_wrong(obj,mes,bl){
	bl?validTip.right(obj,mes):validTip.wrong(obj,mes);
}
function check_single(lg,obj,bl,al){
	var _obj = $(obj),sv = $.trim(_obj.val()),regx = mess(lg,2);
	if(bnu(sv)){
		if(al){
			check_select(lg,false);
		}else{
			validTip.wrong(_obj,mess(lg,1));
		}
		return false;
	}else if(!bnu(regx)&&!regx.test(sv)){
		validTip.wrong(_obj,mess(lg,3));
		return false;
	}else if(bl){
		if(al){
			check_select(lg,true);
		}
		validTip.right(_obj,"");
		return true;
	}else{
		var status=false;
		$.ajax({
			url:mess(lg,5),
			type:'post',
			async:false,
			data: mess_dat(lg,sv),
			error:function(){
				validTip.wrong(_obj,mess(null,0));
				status=false;
			},
			success:function(data){
				if(data==0){
					validTip.right(obj,mess(lg,4));
					status=true;
				}else{
					validTip.wrong(obj,mess(lg,4));
					status=false;
				}
			}
		});
		return status;
	}
}
function mess_dat(lg,sv){
	return lg==='companyName'?{companyName:sv}:{companyName:sv};
}
;$(function(){
	//省市初始化
	_init_area_for_register();
	//跳转手机注册
	$("#phone_tab").unbind('click').bind('click',function(e){
		window.location = "toPhoneRegi.html";
	});
	//跳转邮箱注册
	$("#email_tab").click(function(){
		window.location = "toEmailRegi.html";
	});
	//阅读规则
	$("#register_protocolphone_img").bind('click',function(){ 
	      if($(this).hasClass('checked')){ 
	          $(this).removeClass("checked"); 
	          $("#register_protocolphone").attr("checked",false);
	      }else{ 
	          $(this).addClass("checked");   
	          $("#register_protocolphone").attr("checked",true);
	      }
	 });
	
	//1.企业类型
	$("a.companyType_li").unbind('click').bind('click',function(){
	   if($(this).text()=="其他"){
		    bindcheck([7]);
			$("#companyTypeText").unbind('focus').attr("readonly",false).removeClass("noEditable").focus();
			subcheck([7]);
		}else{
			$("#companyTypeText").attr("readonly",true).addClass("noEditable").val("").unbind('focus').unbind('blur');
		}
	   $("#companyType_value").val($(this).text());
	   $(this).parent().parent().parent().hide();
	   subcheck([2]);
	});
	
	$("div.selectBox span.inputArrow,div.selectBox input.selectInput").not('#city,#city_inputArrow').click(function () {
		var dropDown = $(this).closest('div.selectBox').find('.selectDropDown');
		dropDown.is(':hidden')?dropDown.show():dropDown.hide();
	});
	
	 //2.所属行业
	$("a.profession_li").unbind('click').bind('click',function(el){
	   if($(this).text()=="其他"){
		   	bindcheck([8]);
		   	$("#professionText").unbind('focus').attr("readonly",false).removeClass("noEditable").focus();
		   	subcheck([8]);
		}else{
			$("#professionText").attr("readonly",true).addClass("noEditable").val("").unbind('focus').unbind('blur');
		}
	   $("#profession_selectDropDown").hide();
	   $("#profession_value").val($(this).text());
	   subcheck([3]);
	});
	
	 //3.province4.city
	 $("#city,#city_inputArrow").bind('click',function(el){
	 	if($("#province_selectDropDown").is(':hidden')){
	 		if(!bnu($('#province').val())){
	 			$("#city_selectDropDown").show();
	 		}
		 }else{
			$("#city_selectDropDown").hide();
		 }
	 });

	//点事件
	$(document).click(function(event){
          var e = event ? event : window.event;
          var target = e.srcElement || e.target;
          var $target = $(target);  
          if (!$target.is('#companyType_value') && !$target.is('#companyType_inputArrow') && !$target.parents("div").is('#companyTypeSelectDropDown')) {
              $("#companyTypeSelectDropDown").hide();
          }
          if (!$target.is('#province') && !$target.is('#province_inputArrow') && !$target.parents("div").is('#province_selectDropDown')) {
              $("#province_selectDropDown").hide();
          }
          if (!$target.is('#city') && !$target.is('#city_inputArrow') && !$target.parents("div").is('#city_selectDropDown')) {
              $("#city_selectDropDown").hide();
          }
          if (!$target.is('#profession_value') && !$target.is('#profession_inputArrow') && !$target.parents("div").is('#profession_selectDropDown')) {
              $("#profession_selectDropDown").hide();
          }
      });
	
	//提交表单
	$("#submitBtn").click(function (){
		 var blbl = subcheck([0,1,2,3,4,5]);
		 var alal = subTextcheck();
		 if(blbl&&alal){
			if(!$("#register_protocolphone").attr("checked")){
			    ui.error("请仔细阅读并确认该注册服务条款!");
				return;
			}
			if(!checkVersion()){
				uic.longMess("您的认证信息已经审核完成，不能重复提交认证信息。请进入用户信息进行修改!");
				return;
			}
			$(this).unbind('click');
			$('#submitform').submit();
		}
	});
	
});
function checkVersion(){
	if($('#flag').val()==1){
		var version = $('#version').val();
		if(bnu(version)){return true;};
		var status = false;
		$.ajax({
			url:'checkVersion.html',
			type:'post',
			async:false,
			data: {id:$('#id').val()},
			success:function(data){
				if(data==version){
					status=true;
				}else{
					status=false;
				}
			}
		});
		return status;
	}
	return true;
	
}