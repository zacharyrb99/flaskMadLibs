"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, id, title, words, text):
        """Create story with words and template text."""

        self.id = id
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started
story1 = Story(
    "folktale",
    "Once Upon a Time",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "scientist",
    "Albert Einstein",
    ["place", "adjective_1", "adjective_2", "celebrity_1", "celebrity_2", "noun_1", "noun_2", "noun_3", "plural_noun_1", "plural_noun_2", "plural_noun_3", "plural_noun_4", "plural_profession"],
    """Albert Einstein, the son of {celebrity_1} and {celebrity_2}, was born in Ulm, Germany, in 1879.
    In 1902, he had a job as assistant {noun_1} in the Swiss patent office and attended the
    University of Zurich. There he began studying atoms, molecules, and {plural_noun_1}. He developed the 
    theory of {adjective_1} relativity, which expanded the phenomena of sub-atomic {plural_noun_2} and 
    {adjective_2} magnetism. In 1921, he won the Nobel price for {plural_noun_3} and was the director of 
    theoretical physics at the Kaiser Wilhelm {noun_2} in Berlin. In 1933, when Hitler became Chancellor 
    of {place}, Einstein came to America to take a post at Princeton Institute for {plural_noun_4}, where 
    his theories helped America devise the first atomic {noun_3}. There is no question about it: Einstein 
    was one of the most brilliant {plural_profession} of our time."""
)

story3 = Story(
    "zoo visit",
    "Visting the Zoo",
    ["adjective_1", "adjective_2", "adjective_3", "adjective_4", "animal_1", "animal_2", "funny_noise_1", "funny_noise_2", "body_part", "plural_animal", "plural_noun_1", "plural_noun_2", "plural_noun_3", "type_of_liquid"],
    """Zoos are places where wild {plural_noun_1} are kept in pens or cages so that {plural_noun_2} 
    can come and look at them. There are two zoos in New York, one in the Bronx and one in 
    {adjective_1} Park. The Park zoo is built around a large pond filled with clear sparkling 
    {type_of_liquid}. You will see several {plural_animal} swimming in the pond and eating fish. 
    When it is a feeding time, all the animals make {adjective_2} noises. The elephant goes {funny_noise_1} 
    and the turtledoves go {funny_noise_2}. In one part of the zoo, there are {adjective_3} gorillas who 
    love to eat {plural_noun_2}. In another building, there is a spotted African {animal_1} that is 
    so fast it can outrun a {animal_2}. But my favorite animal is the hippo. It has a huge {body_part} 
    and eats 50 pounds of "{plural_noun_3} a day. You would never know that, technically, it's 
    nothing but an oversize {adjective_4} pig."""
)

stories = {story.id: story for story in [story1, story2, story3]}
