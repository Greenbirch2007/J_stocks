# coding=utf-8
from selenium import webdriver
from time import time
import time
driver = webdriver.Chrome()

# 把大阪地区的好好了解一下
hp_list = [
"http://www.aioi-sec.com/","http://www.sittsec.co.jp/","http://www.iwaicosmo.co.jp/","http://www.eiwa-sec.co.jp/","http://www.ace-sec.co.jp/","http://www.okayasu-sec.co.jp","https://www.okayasu-shoji.co.jp/","https://www.kyogin-sec.co.jp/","http://www.kosei.co.jp/","http://sasayama-sec.co.jp/","http://www.naito-sec.co.jp/","https://www.nanto-sec.co.jp","http://www.nishimura-sec.co.jp/","http://www.banyo-sec.co.jp/","http://www.hikarishoken.com/","http://www.hibiki-sec.co.jp","http://www.hirota-sec.co.jp","http://www.maruchika-shoken.co.jp",


]


all_J = [
"http://www.utsumiya.co.jp","http://www.usuki.co.jp","http://www.traderssec.com","http://www.toyo-sec.co.jp/","http://www.tokaitokyo.co.jp/","http://www.toho-sec.co.jp","http://www.tochigintt.co.jp","http://www.tobu-sec.jp/","http://www.tg-sec.co.jp/","http://www.superfund.co.jp/","http://www.starts-sc.com","http://www.ssga.com/","http://www.spc-sec.co.jp","http://www.smbcnikko.co.jp/","http://www.sjnk-dc.co.jp/","http://www.sittsec.co.jp/","http://www.shizuokatokai-sec.co.jp","http://www.shizugintm.co.jp/","http://www.shin-ogaki.co.jp/","http://www.shinkinsec.jp/","http://www.shikoku-alliance-sec.co.jp","http://www.secjp.co.jp/","http://www.sc.mufg.jp/","http://www.sbiprime.com","http://www.sankyo-sec.co.jp","http://www.sanen-sec.co.jp/","http://www.retela.co.jp","http://www.rakuten-sec.co.jp","http://www.pwm.co.jp/","http://www.phillip.co.jp/","http://www.pawa.co.jp","http://www.one-asia.co.jp/","http://www.okigin-sec.co.jp/","http://www.okayasu-sec.co.jp","http://www.okasan-online.co.jp","http://www.okasan.co.jp","http://www.okachi-sec.co.jp/","http://www.nomura.co.jp","http://www.nissan-sec.co.jp","http://www.nishimura-sec.co.jp/","http://www.news-sec.co.jp","http://www.nctt.co.jp/","http://www.nakahara-sec.co.jp","http://www.naito-sec.co.jp/","http://www.musashi-sec.co.jp/","http://www.morganstanley.com/im/ja-jp/japanese-investor.html","http://www.morganstanley.co.jp/index.html","http://www.moneypartners.co.jp","http://www.money-design.com","http://www.monex.co.jp/","http://www.mizuho-sc.com/","http://www.mitsui-sc.co.jp/","http://www.mitsui-ai.com/ja/index.html","http://www.mitoyo-sec.co.jp/","http://www.mito.co.jp","http://www.miraisec.co.jp/","http://www.miki-sec.co.jp/","http://www.midori-sec.co.jp/","http://www.meiwa-sec.co.jp/","http://www.mebuki-sec.co.jp","http://www.mcp-am.jp/","http://www.mcasset.com","http://www.matsui.co.jp/","http://www.masumo.co.jp/","http://www.marusan-sec.co.jp","http://www.marukuni.co.jp","http://www.maruhachi-sec.co.jp/","http://www.maruchika-shoken.co.jp","http://www.madison-sec.co.jp/","http://www.lockehallard.com","http://www.live-sec.co.jp","http://www.leonteq.com","http://www.leading-sec.com/","http://www.kyowa-sec.co.jp/","http://www.kyokuto-sec.co.jp","http://www.koyo-sec.co.jp/","http://www.kotobuki-sec.co.jp","http://www.kosei.co.jp/","http://www.kkr.com/ja","http://www.kimurasec.co.jp","http://www.kanetsufx.co.jp/","http://www.kagawa-sc.co.jp/","http://www.kabu.com","http://www.jsa-hp.co.jp","http://www.jpmorgan.com/","http://www.j-pa.co.jp/","http://www.jbond.co.jp/","http://www.japan.ml.com/main_j.asp","http://www.iwaicosmo.co.jp/","http://www.isurugi-sec.co.jp","http://www.is-sec.co.jp/","http://www.isec.jp","http://www.irjapan.net/index.html","http://www.invast.jp/","http://www.interactivebrokers.co.jp","http://www.imamura.co.jp","http://www.ig.com","http://www.ichiyoshi.co.jp","http://www.hirota-sec.co.jp","http://www.hirogin-sec.co.jp/","http://www.hikarishoken.com/","http://www.hibiki-sec.co.jp","http://www.gunginsec.co.jp","http://www.gs.com","http://www.goginsec.co.jp","http://www.futanami-sec.co.jp","http://www.fukuoka-sec.co.jp","http://www.fujitomi.co.jp/","http://www.fpgsec.jp/","http://www.fidelity.jp","http://www.ewarrant.co.jp","http://www.evofinancialgroup.com/ejs/","http://www.eiwa-sec.co.jp/","http://www.ehime-sc.co.jp","http://www.daiwa.co.jp/","http://www.daishi-sec.co.jp","http://www.daiman.co.jp","http://www.daikumamoto.co.jp","http://www.ctsec.co.jp","http://www.click-sec.com/","http://www.citigroupglobalmarkets.co.jp","http://www.chugin-sec.jp/","http://www.chibagin-sec.co.jp/","http://www.centrade.co.jp/","http://www.capital.co.jp","http://www.cantor.com/global/asia/Japan/","http://www.bb.jbts.co.jp/","http://www.barclays.co.jp/","http://www.banyo-sec.co.jp/","http://www.bansei-sec.co.jp/","http://www.axa-im.co.jp","http://www.ark-sec.co.jp/","http://www.aozora-sec.co.jp/","http://www.anz.co.jp/about-us/profile/","http://www.ando-sec.co.jp/","http://www.alliancebernstein.co.jp/","http://www.akatsuki-sc.com/","http://www.aizawa.co.jp","http://www.airssea.co.jp","http://www.aioi-sec.com/","http://www.ace-sec.co.jp/","http://www.8securities.co.jp","http://www.82sec.co.jp","http://www.1ban.co.jp","http://www.105sec.co.jp/","http://tahara-sec.co.jp","https://www.yjfx.jp/","https://www.yamawa-sec.co.jp","https://www.tsumiki-sec.com","https://www.shonaisc.co.jp/","https://www.sbisec.co.jp/","https://www.rbccm.com/japan/jp/cid-244468.html","https://www.onetapbuy.co.jp/","https://www.okpremiere-sec.co.jp/","https://www.okayasu-shoji.co.jp/","https://www.okasan-niigata.co.jp/","https://www.ni-sec.com/","https://www.nanto-sec.co.jp","https://www.m2j.co.jp","https://www.kyushu-fg-sec.co.jp","https://www.kyogin-sec.co.jp/","https://www.hs-sec.co.jp/","https://www.home.saxo/ja-jp","https://www.hokuyo-sec.co.jp/","https://www.hokuhokutt.co.jp/","https://www.ezinvest-sec.jp/","https://www.daisenhinomaru.co.jp/","https://www.daiko-sb.co.jp","https://www.credit-suisse.com/jp/ja.html","https://www.assetmanagement.hsbc.co.jp","https://www.77sec.co.jp/","https://smartplus-sec.com/","https://naganosec.co.jp/","https://nab.com.au/japansecuritiesjp","http://shin-sec-sakamoto.jp/","http://shimadai.com","https://funds.dws.com/jp/","https://folio-sec.com/","http://sec.himawari-group.co.jp/","http://sasayama-sec.co.jp/","https://apac.cib.natixis.com/japan","http://mitasec.com/","http://japan.blackstone.com/","http://hedgefund-sec.com","http://fx.dmm.com","http://fpl-sec.co.jp","http://buko.co.jp",

]
for item in all_J:
    # 如果请求1分钟没有走完就直接break?

    driver.get(item)


    driver.maximize_window()
    time.sleep(3)
    s = time.time()
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(picture_time)

    e = time.time()
    f_time = e - s
    try:
        if int(f_time) >= 30:
            break
        else:

            picture_url=driver.get_screenshot_as_file('/home/w/Desktop/all_J/'+ picture_time +'.png')
            print("%s：截图成功！！！" % picture_url)
    except BaseException as msg:
        print(msg)
