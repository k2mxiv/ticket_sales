from .DBFunction3 import servConnect

def accountingTeamCalc(sel = None) :
    if sel == 'Del' :
        sql = """select p_tb.id, scode, lname, sdate, qty, amt, ifnull(log_file, sales_product.img_file) from(
	select sales_sales.id, scode, lname, sdate, qty, amt, id_tb.log_date, sales_log.img_file as log_file from(
		select id, log_date, min(logno) as logno from sales_sales left join sales_log on (scode = lcode) and (sdate < log_date) and (sdate > product_date) group by id
	)id_tb left join sales_sales on (sales_sales.id = id_tb.id) left join sales_log on id_tb.logno = sales_log.logno where stat = 'Delete'
)p_tb left join sales_product on (scode = pcode) and (sdate > create_date) where lname is not null;"""
    elif sel == 'All' :
        sql = """select p_tb.id, scode, ifnull(lname, pname), sdate, qty, amt, ifnull(log_file, sales_product.img_file) from(
	select sales_sales.id, scode, lname, sdate, qty, amt, id_tb.log_date, sales_log.img_file as log_file from(
		select id, log_date, min(logno) as logno from sales_sales left join sales_log on (scode = lcode) and (sdate < log_date) and (sdate > product_date) group by id
	)id_tb left join sales_sales on (sales_sales.id = id_tb.id) left join sales_log on id_tb.logno = sales_log.logno
)p_tb left join sales_product on (scode = pcode) and (sdate > create_date);"""

    elif sel == 'Liv' :
        sql = """select p_tb.id, scode, ifnull(lname, pname), sdate, qty, amt, ifnull(log_file, sales_product.img_file) from(
	select sales_sales.id, scode, lname, sdate, qty, amt, id_tb.log_date, sales_log.img_file as log_file from(
		select id, log_date, min(logno) as logno from sales_sales left join sales_log on (scode = lcode) and (sdate < log_date) and (sdate > product_date) group by id
	)id_tb left join sales_sales on (sales_sales.id = id_tb.id) left join sales_log on id_tb.logno = sales_log.logno
)p_tb left join sales_product on (scode = pcode) and (sdate > create_date) where pname is not null;"""
    
    val = [list(i) for i in servConnect('fetch', sql)]
    rerult = val
    return rerult

def researchTeamCalc(sel = None) :
    if sel == 'Del' :
        sql = """select pCode, pName, unitPrice, discountRate from product_history where status = 'Delete';"""
        colNam = [['pCode', 'pName', 'unitPrice', 'discountRate']]
    else :
        sql = """select seqNo, sCode, pName, sDate, Qty, Amt from sales right join product on sales.sCode = product.pCode;"""
        colNam = [['seqNo', 'sCode', 'pName', 'sDate', 'Qty', 'Amt']]
    val = [list(i) for i in servConnect('fetch', sql)]
    rerult = [val, colNam]
    return rerult

class accountingAnd :
    def __init__(self) :
        None
    def account(sel = None) :
        val = accountingTeamCalc(sel)        
        return val

    def research(sel = None) :
        val = researchTeamCalc(sel)
        return val