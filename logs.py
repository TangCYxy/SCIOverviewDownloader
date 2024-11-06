import cfgs
import requests
import json
import traceback

defaultHeaders = {
    "Content-Type": "application/json"
}
requests.packages.urllib3.disable_warnings()


def sendToWebhook(msg):
    """
    curl -X POST "https://open.feishu.cn/open-apis/bot/v2/hook/0064d6b6-289b-4f30-b48b-31970e909c1c" -H "Content-Type: application/json" -d "{\"msg_type\":\"text\",\"content\":{\"text\":\"request example\"}}"
    """
    webhookUrl = cfgs.get("webhookUrl", "common")
    if webhookUrl == '':
        return
    try:
        data = {"msg_type": "text", "content": {"text": msg}}
        response = requests.post(webhookUrl, headers=defaultHeaders, data=json.dumps(data), verify=False)
    except Exception as e:
        print(f"sendToWebhook failed, msg is： {msg}, error is {e}")
        traceback.print_exc()


def enhanceLog(*args, **kwargs):
    # 输出到控制台
    print(*args, **kwargs)
    # 输出到飞书
    output = " ".join(map(str, args)) + "\n"
    sendToWebhook(output)
