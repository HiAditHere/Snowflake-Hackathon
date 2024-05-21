'''module imports'''

import replicate

def english_translator(comment):

    '''Function to convert transliterations to english

        Args:
            comment : [str]
                Input comment

        Returns:
            [str] : Translitereated comment

    '''

    prompt_str = f"""
        "Translate the following to english 
        {comment}

        If already in english, dont do anything

        If you are confused, return it as it is

        Limit your response to one sentence max.

    """

    # Geneating translations using snoflake arctic
    response_str = replicate.run(
        "snowflake/snowflake-arctic-instruct",
        input={
            "prompt": prompt_str
        },
    )

    response_str = "".join(response_str)

    return response_str
