from pathlib import Path

from tqdm import tqdm

from utils import gptConnector
import pandas as pd

def generate_poem_gpt4(gpt: gptConnector, poem_description):
    example = ""
    msgs = [{
        "role": "system",
        "content": """he following is a description of a poem writing style I've invented:
```

Mirror Reflections Poetry Style
Stanza Structure: The poem consists of 1-2 stanzas, each containing 4 lines.

Syllable Pattern: Each line follows a specific syllable count pattern. For the first stanza, the pattern is 4-7-7-4. If a second stanza is added, it mirrors the first with a 4-7-7-4 pattern.

Rhyme Scheme: The rhyme scheme is ABBA for each stanza. This means the first and fourth lines rhyme with each other, as do the second and third lines.

Thematic Reflection: The theme of the first two lines should be reflected or inverted in the next two lines. If a second stanza is added, it should explore the opposite aspect or a complementary theme to the first stanza.

Title: The title should be a single word that encapsulates the central theme of the poem.

Language: Use of metaphorical language is encouraged to deepen the reflective quality of the poem.

```

you create poems in the Mirror Reflections style based on a short description a user provides you with.
make sure to abide closely by all the rules I've defined above for this poetry style I invented
your output format: ```\nTitle: <$the poems title>\n<$the poem>\n```
abide strictly by this format.
example: for the input: 'exploring the interplay of light and darkness in the celestial dance of day and night' your output should be: ```\nTitle: Eclipse\nShadows dance
In the moon's silent embrace,
Stars whisper secrets of night,
Sun awaits.

Dreams flicker
In the dawn's gentle caress,
Morning sings hymns of the light,
Night takes flight.\n```"""},
        {"role": "user",
         "content": f"please generate a poem in the Mirror Reflections style based on the following prompt:\n{poem_description}"}
    ]
    poem = gpt.chat_predict(msgs=msgs, model="gpt-4-1106-preview", temp=0.6)
    print(poem)
    return poem

if __name__ == "__main__":
    data_path = Path(r"C:\Users\adamj\PycharmProjects\focousedKD\example projects FKD\Mirror Reflections Poetry Style\data\poems.xlsx")
    df = pd.read_excel(Path(r"C:\Users\adamj\PycharmProjects\focousedKD\example projects FKD\Mirror Reflections Poetry Style\data\title-description.xlsx"))
    gpt = gptConnector()
    new_df = pd.DataFrame(columns=["description", "poem"])
    for description in tqdm(df['description']):
        poem = generate_poem_gpt4(gpt, description)
        new_df = pd.concat([new_df, pd.DataFrame({"description": [description], "poem": [poem]})], ignore_index=True)
        new_df.to_excel(data_path)

