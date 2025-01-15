class MultilineTextChoiceNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Input: Multiline text string with a default empty value
                "multiline_text": ("STRING", {"multiline": True, "default": ""}),
                # Input: Line number to select (1-based index), default is 1
                "selected_line_number": ("INT", {"default": 1, "min": 1, "max": 9999999}),
            },
        }

    # Outputs: an integer (line index) and a string (selected line's content)
    RETURN_TYPES = ("INT", "STRING")
    # Names for the returned values
    RETURN_NAMES = ("choice_index", "selected_text")
    # Function to process the inputs
    FUNCTION = "process"
    # Category under which this node will appear in the UI
    CATEGORY = "Utility"

    def process(self, multiline_text, selected_line_number):
        # Split the input text into a list of non-empty, trimmed lines
        choices = [line.strip() for line in multiline_text.splitlines() if line.strip()]

        # Initialize default return values
        choice_index = 0
        selected_text = ""

        # Check if the selected line number is within the valid range
        if 1 <= selected_line_number <= len(choices):
            # Set the choice_index to the selected line number
            choice_index = selected_line_number
            # Retrieve the text of the selected line (adjusting for 0-based index)
            selected_text = choices[selected_line_number - 1]
        else:
            # If the selected line number is out of range, return defaults
            choice_index = 0
            selected_text = ""

        return (choice_index, selected_text)


# Register the node class with its unique identifier
NODE_CLASS_MAPPINGS = {
    "ThepExcel_AiAngel_MultilineTextChoiceNode": MultilineTextChoiceNode
}

# Define the display name for the node in the UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "ThepExcel_AiAngel_MultilineTextChoiceNode": "ThepExcel_AiAngel_Multiline Text Choice"
}
