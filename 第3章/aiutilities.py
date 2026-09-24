from openai import OpenAI  

#-----------------------------------------------------------------
# 必填：从服务管控页面获取对应服务的APIKey和API Base
api_key = "ak-MmwH2NomJrHzsFTK90dZKaIalUtrkkk4"
api_base = "https://maas-api.cn-huabei-1.xf-yun.com/v2"
client = OpenAI(api_key=api_key, base_url=api_base)
#-----------------------------------------------------------------

def unified_chat_test(messages, use_stream=False, extra_body={}):
    model_id = "spark-x2.5-4b"
    """
    一个统一的函数，用于演示多种调用场景。

    :param model_id: 要调用的模型ID。
    :param messages: 对话消息列表。
    :param use_stream: 是否使用流式输出。
    :param extra_body: 包含额外请求参数的字典，如 response_format。
    """
    try:
        kwargs = {
            "model": model_id,
            "messages": messages,
            "stream": use_stream,
            "temperature": 0.7,
            "max_tokens": 4096,
            "extra_headers": {"lora_id": "0"},  # 调用微调大模型时,对应替换为模型服务卡片上的resourceId
            "extra_body": extra_body,
        }
        if use_stream:
            kwargs["stream_options"] = {"include_usage": True}  # 仅流式请求支持该参数,非流式传会报 10005 invalid request
        response = client.chat.completions.create(**kwargs)

        if use_stream:
            # 处理流式响应
            full_response = ""
            print("--- 流式输出 ---")
            for chunk in response:
                if not chunk.choices:  # 末尾 usage 块无 choices,跳过避免越界
                    continue
                delta = chunk.choices[0].delta
                content = getattr(delta, "content", None)
                if content:
                    print(content, end="", flush=True)
                    full_response += content
            print("\n\n--- 完整响应 ---")
            print(full_response)
            return full_response
        else:
            # 处理非流式响应
            print("--- 非流式输出 ---")
            message = response.choices[0].message
            print(message.content)
            return message.content
    except Exception as e:
        print(f"请求出错: {e}")
        return 0

