class MultilineTextChoiceNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # เปลี่ยนชื่อ selected_choice เป็น selected_line_number
                # และเปลี่ยน type จาก STRING -> INT
                "multiline_text": ("STRING", {"multiline": True, "default": ""}),
                "selected_line_number": ("INT", {"default": 1, "min": 1, "max": 9999999}),
            },
        }

    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("choice_index", "selected_text")
    FUNCTION = "process"
    CATEGORY = "Utility"

    def process(self, multiline_text, selected_line_number):
        # Split multiline text into a list of trimmed choices
        choices = [line.strip() for line in multiline_text.splitlines() if line.strip()]

        # เตรียมตัวแปรคืนค่า
        choice_index = 0
        selected_text = ""

        # ตรวจสอบว่า line_number ที่ส่งเข้ามาไม่เกินจำนวนบรรทัด
        if 1 <= selected_line_number <= len(choices):
            choice_index = selected_line_number
            selected_text = choices[selected_line_number - 1]
        else:
            # ถ้า line_number ไม่อยู่ในช่วงที่มีใน choices
            choice_index = 0
            selected_text = ""

        return (choice_index, selected_text)


# Node registration
NODE_CLASS_MAPPINGS = {
    "ThepExcel_AiAngel_MultilineTextChoiceNode": MultilineTextChoiceNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ThepExcel_AiAngel_MultilineTextChoiceNode": "ThepExcel_AiAngel_Multiline Text Choice"
}
