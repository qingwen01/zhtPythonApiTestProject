# -*- coding: utf-8 -*-
from app.models import db
from sqlalchemy.sql import func
from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash

class OpenidInfos(db.Model):
    '''用户微信基本信息'''

    __tablename__ = "openid_infos"

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    openid = db.Column(db.String(50), primary_key=True, comment=u'openid')
    mobile = db.Column(db.String(20), comment=u'手机号')
    nick_name = db.Column(db.String(200), comment=u'昵称')
    sex = db.Column(db.String(20), comment=u'性别')
    city = db.Column(db.String(100), comment=u'城市')
    province = db.Column(db.String(100), comment=u'省份')
    country = db.Column(db.String(100), comment=u'国家')
    subscribe_time = db.Column(db.String(20), comment=u'最后关注时间')
    subscribe_scene = db.Column(db.String(100), comment=u'关注渠道')
    subscribe = db.Column(db.String(10), comment=u'是否关注公众号')
    is_push = db.Column(db.String(200), comment=u'是否推送模板消息')
    create_time = db.Column(db.DateTime, server_default=func.now(), comment=u'添加时间')
    up_time = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), comment=u'添加时间', )
    is_active = db.Column(db.Integer, server_default='0', comment=u'状态: 0 正常; 1 异常')

    __table_args__ = ({'comment': '用户微信基本信息'})  # 添加表注释

    def __repr__(self):
        return "openid: %s" % self.id