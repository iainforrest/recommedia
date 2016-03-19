//<script>
(function(){
	var new_campaigns = {"221837":{"ad_shown":false,"pid":"221836","ctype":"campaign","activations":[{"activation":"timer","prop":"","val":"0"}],"overlay":"none","coverlay":"none","ctop":"none","cbottom":"genie","bottom":"genie","callout":"none","callout_t":"","callout_pos":"rm","callout_anchor_pos":"lm","callout_voffset":"0","callout_hoffset":"0","acas":0,"top":"none","overlay_teleport_html":"","overlay_teleport_type":"_blank","opacity":0.9,"color":"#000000","close_button_delay":0,"show_close":0,"show_close_step":0,"close_redirect_url":"","close_redirect_type":"_self","activation_delay":0,"closed_no_show":0,"ipc":0,"mas":0,"mao":0,"map":0,"iao":"0","rao":"0","tvao":"0","is_ec":true,"is_api":true,"is_man":0,"ad_auto_close":0,"activation_offset":0,"header_top_nano":0,"header_bottom_nano":0,"type":"agilityzone","hbna":"0","hbnbg":"0","htna":"0","htnbg":"1","ad_visible":false,"osfn":"","tes":"1","te":"no_effect","t_valign":"top","b_valign":"bottom","qbxtest":false,"submission_redirect":"","submission_redirect_delay":2,"osfn_website":"","supress_overlay":0,"repress_overlay":0,"supress_top":0,"repress_top":0,"supress_bottom":0,"repress_bottom":0,"ng":0,"images":[],"edw":0,"event_js":"{\"activation\":\"jQuery('#tf-popular-in-category-2').before(jQuery('#campaign_' + campaign_id  + '_container_bottom').css({position: 'relative', left: '-11px', marginBottom: '15px'}));\",\"impression\":\"bouncex.report_ga('impression','eCap  R3  Testing CTA  Access Now  Menu Top');\\n\",\"click\":\"bouncex.report_ga('click','eCap  R3  Testing CTA  Access Now  Menu Top');\\n\",\"submission\":\"bouncex.report_ga('submission','eCap  R3  Testing CTA  Access Now  Menu Top');\\n\\n\\njQuery('<img\\\/>', { height: 1, width: 1, style: 'border-style:none;', alt: '', src: '\\\/\\\/insight.adsrvr.org\\\/track\\\/conv\\\/?adv=tcbqgod&ct=0:qydqv71h&fmt=3' }).appendTo('body');\",\"close\":\"\"}","gbi":false,"control":false,"html":"<style type=\"text\/css\">#bouncex_err_email {   top: -50%;    right: 0%;    font-size: 10px;}<\/style><div class=\"bcx_pusher\" id=\"campaign_221837_pusher_bottom\" style=\"height:370px;display:none;\">&nbsp;<\/div><div data-type=\"bar\" data-valign=\"bottom\" data-align=\"center\" id=\"campaign_221837_container_bottom\" class=\"bouncex_header_bottom center bcx_bottom floating_bar bcx_container bcx_no_effect \" style=\"margin-top:0px;height:370px;display:none;\"><div class=\"bcx_outer\"><div class=\"bcx_inner\" style=\"overflow:hidden;width:320px;height:370px;\"><div class=\"bcx_ie_fix\"><\/div><div><a target=\"_top\" id=\"bcx_close_221837_bottom\" class=\"bouncex_close bcx_close_header_bottom size_75  top_right center  bcx_close_\" href=\"javascript:close_bouncex_ad(221837);\"><span>Close<\/span><\/a><iframe name=\"bcx_221837_iframe_bottom\" id=\"bcx_221837_iframe_bottom\" horizontalscrolling=\"no\" verticalscrolling=\"no\" width=\"100%\" height=\"100%\" frameborder=\"0\" vspace=\"0\" hspace=\"0\" marginwidth=\"0\" marginheight=\"0\" allowTransparency=\"true\" target=\"_parent\" src=\"http:\/\/api.bounceexchange.com\/bounce\/iframe_campaign\/221837?mode=0&website_id=1313&device_type=d&cv_id=&visit_id=1453019856597753&height=647&w=320px&h=370px&width=1280&campaign_id=221837&cvt=1453019856&fsa=1452880414&scale=1&pos=header_bottom\"><\/iframe><\/div><\/div><\/div><\/div>","styles":""}};
	bouncex.brandStyles = false;
	bouncex.webfonts = false;

	if (typeof bouncex.loadWebfonts === 'function') {
		bouncex.loadBrandStyles();
		bouncex.loadWebfonts();
	}
	bouncex.unload_campaigns();
	
	
	var campaign_added = false;
	for(var ca_id in new_campaigns){
		if(new_campaigns.hasOwnProperty(ca_id)){
			if(!bouncex.cookie.campaigns){
				bouncex.cookie.campaigns = {};
			}
			if(!bouncex.cookie.campaigns[ca_id]){
				campaign_added = true;
				bouncex.cookie.campaigns[ca_id] = {lvt:bouncex.cookie.lvt, vv:0};
			}
		}
	}
	if(campaign_added){
		bouncex.setBounceCookie();
	}
	
	for(var ca_id in bouncex.campaigns){
		if(bouncex.campaigns.hasOwnProperty(ca_id)){//copy state vars
			if(new_campaigns[ca_id]){
				new_campaigns[ca_id].ap = bouncex.campaigns[ca_id].ap;
				new_campaigns[ca_id].repressed = bouncex.campaigns[ca_id].repressed;
			}
			if(new_campaigns[ca_id]&&
				bouncex.campaigns[ca_id].ad_visible&&
				new_campaigns[ca_id].html.replace(/fsa=(\d+)&|width=(\d+)&|height=(\d+)&/gi,'')==bouncex.campaigns[ca_id].html.replace(/fsa=(\d+)&|width=(\d+)&|height=(\d+)&/gi,'')){
								new_campaigns[ca_id] = bouncex.campaigns[ca_id];
				bouncex.campaigns[ca_id].activated = false;
				bouncex.activate_campaign(ca_id);

			}else{
				bouncex.destroy_ad(ca_id);
			}
			
		}
	}

	bouncex.campaigns = new_campaigns;
	new_campaigns = {};
	//bouncex.cookie = {"fvt":1441707907,"vid":1453019856597753,"ao":16,"as":1,"vpv":1,"d":"d","lp":"http%3A%2F%2Ffourhourworkweek.com%2Fpodcast%2F","r":"","cvt":1453019856,"gcr":98,"m":0,"sid":0,"campaigns":{"208748":{"vv":1,"lvt":1453020157,"lavid":1453019856597753,"la":1453020157,"fsa":1450604479,"av":1,"as":1,"ao":4},"221837":{"vv":0,"lvt":1452880441,"lavid":1452880115351325,"la":1452880441,"fsa":1452880414,"av":0,"as":0,"ao":2},"224794":{"vv":1,"lvt":1453020279,"lavid":1453019856597753,"la":1453019982,"fsa":1453019982,"av":1,"as":1,"ao":1,"wc":1453020343},"224796":{"vv":5,"lvt":1452880565,"lavid":1452880115351325,"la":1452880444,"fsa":1452880444,"av":1,"as":1,"ao":1}},"lvt":1453020279,"ibxt":"MTQ0MTcwNzUxMzIxOTQxMQ%3D%3D"};
	bouncex.debug = false;
		bouncex.setBounceCookie();
	if (bouncex.campaigns) {
		bouncex.initActivationFuncs();
	}
	if(bouncex.campaigns && !bouncex.css_added){
		bouncex.init_lightbox();
	}
	}());
