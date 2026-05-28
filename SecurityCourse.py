#script by MapleCake NJUPT2025管院新生
#2025级新生防范电信网络诈骗系列微课

import requests
import json

token=input("请输入你的X-Access-Token：")

def finish_class(courseid,sectionid,knowid,time):
    headers = {
        'Origin': 'https://study.njupt.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://study.njupt.edu.cn/web/training/player?id=1976850292003586049',
        'content-type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        'X-Access-Token': token
    }
    json_data = {'courseId': courseid,'sectionId': sectionid,'knowId': knowid,'playTime':time,'end':1,"intervalTime":5,"currentPage":1}
    responses = requests.post(url='https://study.njupt.edu.cn/service-api/app/study/my/course/start',headers=headers,json=json_data)
    print(responses.text)
    return responses



def main():
    # 获取文件
    #json_data = requests.get(url='https://study.njupt.edu.cn/service-api/app/study/course/info?_t=1761532819&id=1976850292003586049').text
    # 解析JSON数据
    data = json.loads(json_data)
    # 创建一个空列表来存储所有ID
    sectionid_list = []

    knowid_list1 = []
    time_list1 = []

    knowid_list2 = []
    time_list2 = []
    # 添加顶层result的ID
    id=data['result']['id']
    part=1
    # 遍历sectionList
    for section in data['result']['sectionList']:
        # 遍历每个section中的knowList
        sectionid_list.append(section['id'])
        for knowledge in section['knowList']:
            # 添加knowledge的ID
            match part:
                case 1:
                    print("正在处理第1部分")
                    knowid_list1.append(knowledge['id'])
                    time_list1.append(knowledge['knowHour'])
                case _:
                    print("正在处理第2部分")
                    knowid_list2.append(knowledge['id'])
                    time_list2.append(knowledge['knowHour'])
        part=part+1
    # # 打印结果
    # print("所有ID列表:")
    # print(id)
    # print("_________________________")
    # for id in sectionid_list:
    #     print(id)
    # print("_________________________")
    # for id2 in knowid_list:
    #     print(id2)

    courseid=id
    for i in range(len(sectionid_list)):
        sectionid=sectionid_list[i]
        match i:
            case 0:
                knowid_list=knowid_list1
                time_list=time_list1
            case _:
                knowid_list=knowid_list2
                time_list=time_list2
        for j in range(len(knowid_list)):
            knowid=knowid_list[j]
            time=time_list[j]
            response=finish_class(courseid,sectionid,knowid,time)
            print("完成课程成功")
            print(response.text)

if __name__ == "__main__":
    json_data = '''{
    "success": true,
    "message": "操作成功！",
    "code": 200,
    "result": {
        "id": "1976850292003586049",
        "name": "2025级新生防范电信网络诈骗系列微课",
        "courseType": "2025级新生防范电信网络诈骗系列微课",
        "pathTypeName": "2025级新生防范电信网络诈骗系列微课",
        "createBy": "W20231687",
        "createTime": "2025-10-11 11:20:12",
        "courseImg": "https://study.njupt.edu.cn/njupt/course/20251011/ff80808199841ab00199d147a4a40cb2.png",
        "mustStatus": 1,
        "limitType": "1",
        "courseDesc": null,
        "courseHour": 5546,
        "courseScore": 0.0,
        "finishType": 3,
        "finishPages": 0,
        "examId": "1976849161600974850",
        "startTime": "2025-10-01 00:00:00",
        "endTime": "2099-12-31 00:00:00",
        "showStudyTime": null,
        "playStatus": 0,
        "learnStatus": 0,
        "courseSource": null,
        "sectionList": [
            {
                "id": "1976850709680766978",
                "parentId": "0",
                "name": "防诈骗安全教育课",
                "sectionHour": null,
                "childs": [],
                "knowList": [
                    {
                        "id": "1695350800412368898",
                        "knowName": "1-断卡行动",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 559,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff8080818985e0ae018a30ee9fe41877.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 46.920148,
                        "finishBfb": "0.08",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695351925614104578",
                        "knowName": "2-刷单诈骗-1",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 630,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff808081897d8dce018a30f3343c5ad7.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 7.339618,
                        "finishBfb": "0.01",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695352225603313665",
                        "knowName": "3-刷单诈骗-2",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 493,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff8080818985e0ae018a30f42ac41878.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695352488904941570",
                        "knowName": "4-虚假购物诈骗",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 467,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff808081897d8dce018a30f5501f5ad8.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695352962953564162",
                        "knowName": "5-虚假购物",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 528,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff808081897d8dce018a30f6319d5ad9.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695353323458187266",
                        "knowName": "6-注销贷款账户",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 499,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff808081897d8dce018a30f7f3b85ada.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695353549183045633",
                        "knowName": "7-冒充熟人诈骗",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 509,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff8080818985e0ae018a30f91e401879.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1695353758843719681",
                        "knowName": "8-冒充公检法诈骗",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 537,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20230826/ff808081897d8dce018a30f9f61c5adb.mp4",
                        "courseSectionId": "1976850709680766978",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    }
                ]
            },
            {
                "id": "1976850857752281089",
                "parentId": "0",
                "name": "小柚特烦恼系列安全课",
                "sectionHour": null,
                "childs": [],
                "knowList": [
                    {
                        "id": "1831256547288780801",
                        "knowName": "1-小柚特烦恼之：偶遇假老师，骗收学杂费",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 55,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240904/ff8080818f5e153b0191bc4563d517b1.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 55.0,
                        "finishBfb": "100",
                        "finishStatus": 1,
                        "pauseTime": null
                    },
                    {
                        "id": "1831498273165172738",
                        "knowName": "2-小柚特烦恼之：“学长”来推销，柚子中了招",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 59,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfb49c4c4ba9.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831498546147254274",
                        "knowName": "3-小柚特烦恼之：兼职套路深，专坑大学生",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 80,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfb5d6054baa.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831498671263342594",
                        "knowName": "4-小柚特烦恼之：天上掉馅饼，刷单不能信",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 116,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfb644c34bab.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831498786577342466",
                        "knowName": "5-小柚特烦恼之：“同城约会”，柚某被骗5000元的惊人内幕！",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 108,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfb6b7053cd1.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831498998809124865",
                        "knowName": "6-小柚特烦恼之：“土豪”买账号，“硬控”柚子一整天",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 52,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfb77f9a4bac.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499119261147138",
                        "knowName": "7-小柚特烦恼之：网上交易需谨慎，陌生链接不要点",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 87,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfb7f0a53cd3.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499218221555714",
                        "knowName": "8-小柚特烦恼之：“客服”要退款，盯上柚子生活费",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 91,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfb84e183cd4.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499376376176641",
                        "knowName": "9-小柚特烦恼之：冒充公检法，“安全账户”不安全",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 102,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfb8dc0c4bad.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499511357267969",
                        "knowName": "10-小柚特烦恼之：不贪蝇头小利，拒做诈骗帮凶",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 89,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfb961bb4bae.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499618676924417",
                        "knowName": "11-小柚特烦恼之：低头过马路，险些出事故",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 39,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfb9bd963cd5.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 39.0,
                        "finishBfb": "100",
                        "finishStatus": 1,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499748968861697",
                        "knowName": "12-小柚特烦恼之：防止饿肚子的小秘诀，外卖柜或当面取餐",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 77,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfba3adc3cd6.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499864320610306",
                        "knowName": "13-小柚特烦恼之：车辆不上锁，盗贼随时来",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 63,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfbaaa7a4baf.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831499966837788673",
                        "knowName": "14-小柚特烦恼之：占座用电脑，瞬间被偷跑",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 43,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfbb05a94bb0.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831500099423932417",
                        "knowName": "15-小柚特烦恼之：球场争高低，忽视了手机",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 56,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfbb7e413cd7.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831500196765339649",
                        "knowName": "16-小柚特烦恼之：占座用书包，小偷马上到",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 46,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f5e153b0191bfbbe23c4bb1.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    },
                    {
                        "id": "1831500332295806978",
                        "knowName": "17-小柚特烦恼之：全民禁毒，你我同行",
                        "knowSource": "安全教育",
                        "knowType": "1",
                        "knowHour": 161,
                        "knowScore": 0.0,
                        "knowUrl": "https://study.njupt.edu.cn/njupt/knowledge/20240905/ff8080818f497bca0191bfbc524a3cd8.mp4",
                        "courseSectionId": "1976850857752281089",
                        "finishHour": 0.0,
                        "finishBfb": "0",
                        "finishStatus": 0,
                        "pauseTime": null
                    }
                ]
            }
        ]
    },
    "timestamp": 1761532165209
}'''
    main()
