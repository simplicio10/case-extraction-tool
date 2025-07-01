def basic_initial_prompt(brief):
    return f"""
    Please find and return every case, statute, and court rule in this brief: {brief}. 
    Return the total count of all cases as a single number in <case_count> tags.
    """

def better_initial_prompt_1(brief):
    #Improves on basic output by using double_check tags
    return f"""
    Included below is a legal brief:
    <brief>
    {brief}
    </brief>

    Please carefully review the brief and provide me a list of every case, court rule, or statute that is cited in the brief.
    When a case is cited, only list the main case citation. 
    
    <example>
    For example, if the citation is 
    "Zadvydas v. Davis, 533 U.S. 678, 719 (2001) (citing Shaughnessy v. United States ex rel. Mezei, 345 U.S. 206 (1953)),"
    you should only list Zadvydas v. Davis, 533 U.S. 678, 719 (2001), the principal case being cited.
    </example>

    Before answering, you should double-check your work to make sure you have not missed a case or included one that is not present.
    Please put your double-checked work in <double_check> tags and your final list of cases in <final_list> tags.
    All cases should go in <case> tags, all statutes in <statute> tags, and all court rules in <rule> tags.
    Finally, provide the total number of cases in <case_count> tags. Please include only a number inside the <case_count> tags.
    """

def better_initial_prompt_2(brief):
    #Improves on basic output by using thinking tags
    return f"""
    Included below is a legal brief:
    <brief>
    {brief}
    </brief>

    Please carefully review the brief and provide me a list of every case, court rule, or statute that is cited in the brief.
    When a case is cited, you should not list any quoted cases in parentheses. For example, if the citation is 
    "Zadvydas v. Davis, 533 U.S. 678, 719 (2001) (citing Shaughnessy v. United States ex rel. Mezei, 345 U.S. 206 (1953)),"
    you should only list Zadvydas v. Davis, 533 U.S. 678, 719 (2001).

    Think step by step. As you think, put your thoughts in <thinking> tags and your final list of cases in <final_list> tags.
    All cases should go in <case> tags, all statutes in <statute> tags, and all court rules in <rule> tags.
    Finally, provide the total number of cases in <case_count> tags. Please include only a number inside the <case_count> tags.
    """

def refactored_prompt(brief):
    #Tries to refactor Prompt 2 and 3
    return f"""
    Included below is a legal brief:
    <brief>
    {brief}
    </brief>

    Please carefully review the brief and provide me a list of every case that is cited in the brief.

    When a case is cited, you should not list any quoted cases in parentheses. 
    <example>
    For example, if the citation is 
    "Zadvydas v. Davis, 533 U.S. 678, 719 (2001) (citing Shaughnessy v. United States ex rel. Mezei, 345 U.S. 206 (1953)),"
    you should only list Zadvydas v. Davis, 533 U.S. 678, 719 (2001).
    </example>

    Think step by step. As you think, put your thoughts in <thinking> tags and your final list of cases in <final_list> tags.
    All cases should go in <case> tags.
    Finally, provide the total number of cases in <case_count> tags. Please include only a number inside the <case_count> tags.
    """