# -*- coding: utf-8 -*-
# @Time : 2022/7/8 18:39
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : pagination.py
# @Project : DataStructureManagementSystem
from utils.SQL.GenerateSQL import GenerateSQL
from django.http import JsonResponse


def pagination(request, sql, *keys):
    exist_page = None
    if request.GET.get('pagination'):
        page = request.GET.get('page')
        count = request.GET.get('count')
        if page is None or count is None:
            return JsonResponse({
                'status': False,
                'errmsg': '开启了分页但没有传入page或者count'
            })
        page = eval(page)
        count = eval(count)
        paginator_status = {'paginator': True, 'page': page, 'count': count}
        sql = GenerateSQL(pagination=paginator_status, operation='SELECT', select_sql=sql).generate_statement
        exist_page = page
    return {
        'sql': sql,
        'exist_page': exist_page
    }
