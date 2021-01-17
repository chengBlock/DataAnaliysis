import decimal
import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import numpy as np

# Create your views here.

# 首页
from app01 import models

def index(request):
    return render(request, "index.html")


def register(request):

    if request.method == 'GET':
        username =request.GET.get('username','none')
        pwd = request.GET.get('pwd','123456')
        models.Admin.objects.create(
            username=username,
            pwd=pwd
        )

        return HttpResponse("%s 注册成功!" % username)


def manage(request):
    # if request.method == 'GET':
    #     return
    manage_list = models.Goods.objects.filter()

    form_data = []

    for obj in manage_list:
        dict_tmp = {}
        dict_tmp['price'] = obj.price
        dict_tmp['number'] = obj.number
        dict_tmp['date'] = obj.date.strftime("%Y-%m-%d")

        if obj.is_sale:
            dict_tmp['is_sale'] = 1
        else:
            dict_tmp['is_sale'] = 0
        form_data.append(dict_tmp)

    print(form_data)
    print(form_data[0])
    print(form_data[0]['price'])
    print(form_data[0]['date'])

    # a_price = manage_list[0].price
    # a_number = manage_list[0].number
    # a_is_sale = manage_list[0].is_sale
    # a_date = manage_list[0].date
    #
    # b_price = manage_list[1].price
    # b_number = manage_list[1].number
    # b_is_sale = manage_list[1].is_sale
    # b_date = manage_list[1].date
    #
    # c_price = manage_list[2].price
    # c_number = manage_list[2].number
    # c_is_sale = manage_list[2].is_sale
    # a_date = manage_list[2].date
    #
    # c_price = manage_list[3].price
    # c_number = manage_list[3].number
    # c_is_sale = manage_list[3].is_sale
    # a_date = manage_list[3].date
    #
    # a_price = manage_list[4].price
    # a_number = manage_list[4].number
    # a_is_sale = manage_list[4].is_sale
    # a_date = manage_list[4].date


    return render(request,"manage.html",{
        "a_price" :form_data[0]['price'],"a_number" :form_data[0]['number'],"a_is_sale" :form_data[0]['is_sale'],"a_time" :form_data[0]['date'],
        "b_price" :form_data[1]['price'],"b_number" :form_data[1]['number'],"b_is_sale" :form_data[1]['is_sale'],"b_time" :form_data[1]['date'],
        "c_price" :form_data[2]['price'],"c_number" :form_data[2]['number'],"c_is_sale" :form_data[2]['is_sale'],"c_time" :form_data[2]['date'],
        "d_price" :form_data[3]['price'],"d_number" :form_data[3]['number'],"d_is_sale" :form_data[3]['is_sale'],"d_time" :form_data[3]['date'],
        "e_price" :form_data[4]['price'],"e_number" :form_data[4]['number'],"e_is_sale" :form_data[4]['is_sale'],"e_time" :form_data[4]['date'],
    })

'''
count = models.Admin.objects.filter(pwd='12').update(
        pwd='123456'
    )
'''

def update(request):

    obj = json.loads(request.POST.get('str'))

    list_A = obj["A"]
    list_B = obj["B"]
    list_C = obj["C"]
    list_D = obj["D"]
    list_E = obj["E"]

    models.Goods.objects.filter(id=1).update(
        price=list_A[0],
        number=list_A[1],
        is_sale=list_A[2],
        date=list_A[3]
    )

    models.Goods.objects.filter(id=2).update(
        price=list_B[0],
        number=list_B[1],
        is_sale=list_B[2],
        date=list_B[3]
    )

    models.Goods.objects.filter(id=3).update(
        price=list_C[0],
        number=list_C[1],
        is_sale=list_C[2],
        date=list_C[3]
    )

    models.Goods.objects.filter(id=4).update(
        price=list_D[0],
        number=list_D[1],
        is_sale=list_D[2],
        date=list_D[3]
    )

    models.Goods.objects.filter(id=5).update(
        price=list_E[0],
        number=list_E[1],
        is_sale=list_E[2],
        date=list_E[3]
    )



    print(type(request.POST.get('str')))
    # print(request.body)
    return HttpResponse('ok')

def echarts(request):
    print('echarts')
    return render(request,"echarts.html")

#处理jquery请求
def getData(request):

    if request.method == 'GET':
        data = {}
        data['categories'] = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
        data['data'] = [5, 20, 36, 10, 10, 20]

        # ensure_ascii=False是告诉json不要对中文进行编码，
        # 不然返回给前端的数据中如果有中文的话会被编码成unicode类型的数据，
        # 导致前端看不到中文
        json_str = json.dumps(data,ensure_ascii=False)
        print(json_str)
        # 使用HttpResponse响应，告知类型，前段自动调用JSON对象解析
    return HttpResponse(json_str,content_type='application/json')


#bar:柱状图
#当前商品价格，goods表
def bar(request):

    goods_list = models.Goods.objects.filter()
    categories = []
    data = []
    dict_tmp = {}

    for obj in goods_list:
        goods_name = obj.goods_name
        price = obj.price
        categories.append(goods_name)
        data.append(price)

    dict_tmp['categories'] = categories
    dict_tmp['data'] = data

    print(dict_tmp)

    json_str = json.dumps(dict_tmp,ensure_ascii=False,cls=DecimalEncoder)
    print(dict_tmp)
    return HttpResponse(json_str,content_type='application/json')

#line:折线图
#不同时间的销量&售价
# 传字典，value为每一列数据
def line(request):

    #存放ABCDE的数据表
    table_list = []

    table_list.append(models.AGR.objects.filter())
    table_list.append(models.BGR.objects.filter())
    table_list.append(models.CGR.objects.filter())
    table_list.append(models.DGR.objects.filter())
    table_list.append(models.EGR.objects.filter())

    #保存tables查出来的字段列表的列表
    list = []
    #遍历每个表
    for table in table_list:
        dict_tmp = {}
        number_tmp = []
        date_tmp = []
        #遍历每个数据项
        for obj in table:
           number_tmp.append(obj.number)
           date_tmp.append(obj.date.strftime('%m/%d'))
        #保存每张表的字段值
        dict_tmp['number'] = number_tmp
        dict_tmp['date'] = date_tmp

        list.append(dict_tmp)


    json_str = json.dumps(list, ensure_ascii=False, cls=DecimalEncoder)
    print(list)
    return HttpResponse(json_str, content_type='application/json')

#pie:饼状图
#销量：custom表
def pie(request):
    a_count = len(models.Custom.objects.filter(goods_name='A'))
    b_count = len(models.Custom.objects.filter(goods_name='B'))
    c_count = len(models.Custom.objects.filter(goods_name='C'))
    d_count = len(models.Custom.objects.filter(goods_name='D'))
    e_count = len(models.Custom.objects.filter(goods_name='E'))
    # print(len(a_count))

    list = [
        {'value':a_count,'name':'A'},
        {'value':b_count,'name':'B'},
        {'value':c_count,'name':'C'},
        {'value':d_count,'name':'D'},
        {'value':e_count,'name':'E'},
        ]

    json_str = json.dumps(list, ensure_ascii=False, cls=DecimalEncoder)
    print(json_str)
    return HttpResponse(json_str,content_type='application/json')


class DecimalEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, decimal.Decimal):
            return float(o)

        super(DecimalEncoder, self).default(o)