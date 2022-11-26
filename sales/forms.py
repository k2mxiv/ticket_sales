from django import forms
from sales.models import Product
from sales.models import Sales

class ProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ['pcode', 'pname', 'jang', 'ptime', 'unitprice', 'discountrate', 'img_file']
        #widgets = {
        #    'pcode' : forms.TextInput(attrs = {'class' : 'form-control'}),
        #    'pname' : forms.TextInput(attrs = {'class' : 'form-control'}),
        #    'unitprice' : forms.TextInput(attrs = {'class' : 'form-control'}),
        #    'discountrate' : forms.TextInput(attrs = {'class' : 'form-control'}),
        #}
        labels = {
            'pcode' : '티켓 코드',
            'pname' : '영화 이름',
            'jang' : '장    르',
            'ptime' : '상영 시간',
            'unitprice' : '가    격',
            'discountrate' : '할 인  율',
            'img_file' : '포 스  터',
        }
        
class SalesForm(forms.ModelForm) :
    class Meta :
        model = Sales
        fields = ['scode', 'sdate', 'qty', 'amt']
        #labels = {
        #    'qty' : '수량',
        #}