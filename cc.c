Action()
{
	web_submit_data("request", 
		"Action=https://sadovod.city/shop/filter/request", 
		"Method=POST", 
		"RecContentType=text/html", 
		"Referer=https://sadovod.city/category/66", 
		"Snapshot=t21.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=page_number", "Value=2", ENDITEM, 
		"Name=id_category", "Value=66", ENDITEM, 
		"Name=price_min", "Value=148.5", ENDITEM, 
		"Name=price_max", "Value=633.5", ENDITEM, 
		"Name=sort", "Value=id_product:desc", ENDITEM, 
		"Name=per_page", "Value=32", ENDITEM, 
		EXTRARES, 
		"Url=https://ieonline.microsoft.com/iedomainsuggestions/ie11/suggestions.ru-RU", "Referer=", ENDITEM, 
		"Url=https://ieonline.microsoft.com/ieflipahead/ie10/rules.xml?mkt=ru-RU", "Referer=", ENDITEM, 
		LAST);

	web_revert_auto_header("Accept-Language");

	web_revert_auto_header("Cache-Control");

	web_add_auto_header("Accept", 
		"*/*");
	return 0;	
}		
