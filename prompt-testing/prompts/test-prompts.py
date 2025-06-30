def basic_initial_prompt(brief):
    return f"""
    Please find and return every case, statute, and court rule in this brief. You should also return a total count of every case, statute, and court rule you find.
    """

def better_initial_prompt_1(brief):
    #Improves on basic output by useing double_check tags
    return f"""
    Included below is a legal brief:
    <brief>
    {brief}
    </brief>

    Please carefully review the brief and provide me a list of every case, court rule, or statute that is cited in the brief. 
    Before answering, you should double-check your work to make sure you have not missed a case or included one that is not present.
    Please put your double-checked work in <double_check> tags and your final list of cases in <final_list> tags.
    All cases should go in <case> tags, all statutes in <statute> tags, and all court rules in <rule> tags.
    Finally, include the number of cases, statutes, and court rules you found in <count> tags. Please include only the number and nothing else.
    """

def better_initial_prompt_1(brief):
    #Improves on basic output by useing double_check tags
    return f"""
    Included below is a legal brief:
    <brief>
    {brief}
    </brief>

    Please carefully review the brief and provide me a list of every case, court rule, or statute that is cited in the brief. 
    Think step by step. As you think, put your thoughts in <thinking> tags and your final list of cases in <final_list> tags.
    All cases should go in <case> tags, all statutes in <statute> tags, and all court rules in <rule> tags.
    Finally, include the number of cases, statutes, and court rules you found in <count> tags. Please include only the number and nothing else.
    """