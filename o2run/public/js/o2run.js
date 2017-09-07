/*
	Developer Navdeep Ghai
*/

o2run = {};


o2run.items = function(){

	var me = this;
	if (!($(".list-group-item"))){
		return false;
	}
	$(".list-group-item").on("click", function(event){
		event.preventDefault();
		group = $(this).attr("group-name");
		me.get_list(group);
		
	});		
}

o2run.items.prototype.get_list = function(group){

	
	this.total = 0;
	var me = this;
	var opts = {};
	var args  = {};
	me.clear();
	args.cmd = "o2run.utils.get_items";
	args.group = group;
	opts.callback = function(data){
		me.callback_get_list(data);
	};
	opts.args = args;
	frappe.call(opts);	

}

o2run.items.prototype.callback_get_list = function(data){
	this.data = data.message? data.message:[];
	if(!this.data.length){
		this.not_found();
		return false;
	}
	this.update_list();
}

o2run.items.prototype.update_list = function(){

	var me = this;
	var total = me.total;
	var data_len = me.data.length;
	var temp_len = data_len - total;
	var temp =  temp_len <= 0?0:temp_len;
	var flag = temp <= 20?temp: temp-20;
	for(var i=total;i<flag; i++){
		
		item = me.data[i];
		me.render(item);
		this.total++;
	}
}

o2run.items.prototype.get_more = function(){
	this.update_list();
}


o2run.items.prototype.render = function(item){
	
	$(".o2run-items").append(item);
	
}

o2run.items.prototype.clear = function(){
	$(".o2run-items").empty();
}


o2run.items.prototype.not_found = function(){
	$(".o2run-items").append(
			"<div class='col-lg-4'><h1> No Item Found</h1></div>"
			);
};

frappe.ready(function(){

	var loc = window.location.pathname.replace("/", "");
	if(loc == "items"){
		new  o2run.items();
	}
});
