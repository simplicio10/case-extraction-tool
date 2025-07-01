def get_count(output, context):
    if "<case_count>" in output:
        try:
            return output.split("<case_count>")[1].split("</case_count>")[0].strip()
        except Exception as e:
            print(f"Error in get_count: {e}")
            return output
    return output

