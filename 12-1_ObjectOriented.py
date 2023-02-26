class Orange:
    def __init__(self, w, c):
        '''weight(重さ)はグラム単位'''
        self.weight=w
        self.color=c
        self.mold=0
        print('Created!!')

    def rot(self, days, temp):
        '''temp(温度)は摂氏'''
        self.mold=days*temp

    def flv(self, sn, sl):
        '''suns(日照時間)はhrs.、soilは肥料の具合'''
        self.suns=sn
        self.soil=sl
        self.taste=sn*sl

or1=Orange(10,'dark orange')
or1.weight=100
or1.color='light orange'
print('or1の重さは%sgです。' %(or1.weight))
print('or1の色味は%sです。' %(or1.color))

print('or1の腐り度(計算前)は%sです。' %(or1.mold))
or1.rot(10,37)
print('or1の腐り度(計算後)は%sです。' %(or1.mold))

## __init__で初期値を定義されないとエラーになるためコメントアウト
##print('\nor1の日照時間は%s時間です。' %(or1.suns))
##print('or1の肥沃度は%sです。' %(or1.soil))
##print('or1の美味しさは%sです。' %(or1.taste))
or1.flv(120,54)
print('\n美味しさ計算しました。')
print('or1の日照時間は%s時間です。' %(or1.suns))
print('or1の肥沃度は%sです。' %(or1.soil))
print('or1の美味しさは%sです。' %(or1.taste))