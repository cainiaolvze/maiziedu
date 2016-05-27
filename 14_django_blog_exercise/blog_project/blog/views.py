# -*- coding:utf-8 -*-
from django.shortcuts import render
import logging
from django.conf import settings
from blog.models import *
#这是django的原生分页类，可以做许多设置
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
#使用setting.py中配置的日志器，一般都在views.py中使用日志器，因为这里都是业务逻辑
logger = logging.getLogger('blog.views')
#用setting数据定义全局变量,返回一个字典
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC}
# Create your views here.
#定义首页方法
def index(request):
    try:
        #分类信息获取（导航数据）
        category_list = Category.objects.all()
        #广告数据
        ad_list = Ad.objects.all()[:5]
        #最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list,10)
        try:
            #获取请求中的页面，默认为1
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            #如果出错默认返回第一页
            article_list = paginator.page(1)
        #添加归档方法
        archive_list = Article.objects.distinct_date()
    except Exception as e:
        #如果出现异常就写入日志
        logger.error(e)
    return render(request,'index.html',locals())
def archive(request):
    try:
        category_list = Category.objects.all()
        ad_list = Ad.objects.all()[:5]
        archive_list = Article.objects.distinct_date()
        #先获取客户端提交的信息
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        #同样的文章分页,但是用到filter()做模糊查询
        article_list = Article.objects.filter\
        (date_publish__icontains = year+'-'+month)
        paginator = Paginator(article_list,10)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    return render(request,'archive.html',locals())

