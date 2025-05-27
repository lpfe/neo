# import os
# import json

# input_dir = "archiv"
# output_file = "merged_output.jsonl"

# def process_dialog(utterances):
#     result = []
#     pair = []
#     for utt in utterances:
#         if utt["role"] == "speaker":
#             pair = [{"role": "user", "content": utt["text"]}]
#         elif utt["role"] == "listener":
#             pair.append({"role": "assistant", "content": utt["text"]})
#             if len(pair) == 2:
#                 result.append({"messages": pair})
#                 pair = []
#     return result

# with open(output_file, "w", encoding="utf-8") as outfile:
#     for root, _, files in os.walk(input_dir):
#         for file in files:
#             if file.endswith(".json"):
#                 filepath = os.path.join(root, file)
#                 with open(filepath, "r", encoding="utf-8") as f:
#                     data = json.load(f)
#                     utterances = data.get("utterances", [])
#                     dialogues = process_dialog(utterances)
#                     for item in dialogues:
#                         json.dump(item, outfile, ensure_ascii=False)
#                         outfile.write("\n")

# print(f"변환 완료! 파일 저장 위치: {output_file}")








import os
import json

def extract_prompt_completion_pairs(utterances):
    pairs = []
    prompt = None
    for utt in utterances:
        if utt["role"] == "speaker":
            prompt = utt["text"]
        elif utt["role"] == "listener" and prompt:
            completion = utt["text"]
            pairs.append({
                "prompt": prompt.strip(),
                "completion": completion.strip()
            })
            prompt = None
    return pairs

def convert_to_chat_format(data_pairs):
    return [
        {
            "messages": [
                {"role": "user", "content": pair["prompt"]},
                {"role": "assistant", "content": pair["completion"]}
            ]
        }
        for pair in data_pairs
    ]

# 입력 폴더와 출력 파일 설정
input_root = "archiv"
output_file = "archiv_converted.jsonl"

all_data = []

# 모든 JSON 파일 탐색 및 처리
for root, _, files in os.walk(input_root):
    for filename in files:
        if filename.endswith(".json"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                utterances = data.get("utterances", [])
                pairs = extract_prompt_completion_pairs(utterances)
                all_data.extend(pairs)

# messages 포맷으로 변환
chat_data = convert_to_chat_format(all_data)

# JSONL로 저장
with open(output_file, "w", encoding="utf-8") as f:
    for item in chat_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"변환 완료: {output_file} 에 저장됨")
