
def setDictData(url):
    # 获取数据
    # ([a-z]\w+) --> '$1'
    dict = {

        'id'          :'100',
        'acode'       :'cn',     # 区域信息   
        'scode'       :'10',     # 内容栏目
        'subscode'    :'0',               # 内容副栏目
        'title'       :'测试文章1',        # 内容标题
        'titlecolor'  :'#333333',      # 标题颜色
        'subtitle'    :'测试副标题',    # 副标题
        'filename'    :'测试链接',      # 自定义路径
        'author'      :'厚德',              # 作者
        'source'      :'本站',              # 来源
        'outlink'     :'原始链接',          # 跳转外链接
        'date'        :'时间',      # 发布时间
        'ico'         :'',        # 缩略图
        'pics'        :'',        # 轮播多图
        'content'     :'文章',      # 内容
        'enclosure'   :'附件',    # 附件
        'keywords'    :'动机',   # 页面关键字
        'description' :'动机', # 页面描述
        'status'      :'1',     # 状态
        'istop'       :'0',     # 置顶
        'isrecommend' :'0',     # 推荐
        'isheadline'  :'0'      # 头条
    }

    return dict

def setSmallDict(id):
    dict = {
        'id' : id,
        'acode':'cn',
        'scode':'10',
        'title':' 测试题目'
    }
    return dict

def dict2SQL(table,my_dict,):
    COLstr=''   #列的字段
    ROWstr=''  #行字段

    ColumnStyle=' VARCHAR(20)'
    for key in my_dict.keys():
        COLstr=COLstr+' '+key+ColumnStyle+','    
        ROWstr=(ROWstr+'"%s"'+',')%(my_dict[key])

    sql4 = "INSERT INTO %s VALUES (%s)"%(table,ROWstr[:-1])
    print(sql4)

    return sql4






