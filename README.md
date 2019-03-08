# J_stocks

技术:
1.表格数据爬取处理
2. 在主程序文件之外引入模块，遍历模块中的列表或集合，简化了代码
3. 集合的使用可以提高遍历效率  学以致用   
4.存在重复爬取的情况，还有就是会变动的数据还是要等到交易闭市之后再爬取，数据才不会变动！  
5. 重复性的标签，如表格数据，按顺序写正则去匹配是无效的,页面中同时有多个表格，糟心啊 
6. 爬取不利，就要重新思考数据源
7. 尝试用pandas read_html去读取一下表格页面，如果不行这个就放弃！
8.   财报可以尝试取大和证券的官网下载决算pdf文件，就变为下载pdf文件，然后批量读取，清洗文件，入库，另外一个方向！


2018.11.18  (用mysql一条并表查询即可！)
SELECT js_FinData.*,js_infos_finanData.industry FROM js_FinData right join js_infos_finanData on js_FinData.id = js_infos_finanData.id ;

注意：
１．信息不匹配时会出现null，所以直接按照id取匹配
２．　workbench多表导出不友好
