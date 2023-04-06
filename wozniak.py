import os
import openai
from interactions import Application
from interactions.http import HttpClient
from interactions.types import OptionChoice, OptionData

# Initialize OpenAI API
openai.api_key = os.getenv("YOUR_OPENAI_API_KEY")

app = Application(
    public_key=os.getenv("YOUR_DISCORD_PUBLIC_KEY"),
    token=os.getenv("YOUR_DISCORD_BOT_TOKEN"),
)

http_client = HttpClient(app.token)

# Command 1: Ping command
@app.command(
    name="ping",
    description="Get the bot's latency",
)
async def ping_command(ctx):
    latency = app.client.latency * 1000
    await ctx.send(f"Pong! {latency:.2f} ms")

# Command 2: Code snippet command
@app.command(
    name="snippet",
    description="Get a code snippet for a specific language",
    options=[
        OptionData(
            name="language",
            description="Choose the programming language",
            type=3,
            required=True,
            choices=[
                OptionChoice(name="Python", value="python"),
                OptionChoice(name="JavaScript", value="javascript"),
                OptionChoice(name="Java", value="java"),
            ],
        )
    ],
)
async def snippet_command(ctx, language: str):
    if language == "python":
        snippet = "```python\nprint('Hello, World!')\n```"
    elif language == "javascript":
        snippet = "```javascript\nconsole.log('Hello, World!');\n```"
    elif language == "java":
        snippet = "```java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println('Hello, World!');\n    }\n}\n```"

    await ctx.send(snippet)

# Command 3: OpenAI GPT command
@app.command(
    name="gpt",
    description="Generate text using GPT",
    options=[
        OptionData(
            name="prompt",
            description="Enter the prompt for GPT-4",
            type=3,
            required=True,
        )
    ],
)
async def gpt_command(ctx, prompt: str):
    response = openai.Completion.create(
        engine="ENTER GPT-4 CODEX HERE",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    output = response.choices[0].text.strip()
    await ctx.send(f"Generated text:\n{output}")

# Command 4: Developer joke command
@app.command(
    name="devjoke",
    description="Get a developer joke",
)
async def devjoke_command(ctx):
    jokes = [
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why do Java programmers wear glasses? Because they don't C#!",
    ]

    await ctx.send(random.choice(jokes))

# Command 5: Count lines of code command
@app.command(
    name="count",
    description="Count the lines of code in a given text",
    options=[
        OptionData(
            name="code",
            description="Enter the code to count lines",
            type=3,
            required=True,
        )
    ],
)
async def count_command(ctx, code: str):
    lines = len(code.split("\n"))
    await ctx.send(f"Lines of code: {lines}")

app.run()
