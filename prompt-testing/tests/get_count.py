def get_count(output, context):
    if "<count>" in output:
        try:
            return output.split("<count>")[1].split("</count>")[0].strip()
        except Exception as e:
            print(f"Error in get_count: {e}")
            return output
    return output

