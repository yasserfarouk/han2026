# HAN 2026 Sample Agent

A sample agent for the HAN 2026 competition built with [NegMAS](https://github.com/yasserfarouk/negmas) and [NegMAS-LLM](https://github.com/autoneg/negmas-llm). You can test your agent using the [HANI](https://github.com/autoneg/hani) interface.

## Quick Start

1. **Install dependencies:** `uv sync` ([details](#installation))
2. **Rename your agent:** Change `mynegotiator.py` → `your_agent.py` and `MyNegotiator` → `YourAgent` ([details](#getting-started-rename-your-agent))
3. **Implement your agent:** Edit your renamed file ([details](#implementing-your-agent), [examples](#example-agents))
4. **Test locally:** against LLM negotiators `han2026 run` and `han2026 tournament` ([details](#usage-from-the-command-line))
5. **Test locally:** against human negotiators `hani --dev`.
5. **Submit:** Zip and upload to the competition site ([details](#submission))

> [!NOTE]
> We **HIGHLY recommend** that you follow the whole process from installation to submission once you download this skeleton submitting the sample negotiator as your own submission to understand the whole process and save a lot of time later. The whole process should take no more than *5min* to try. If you face any issues in the submission you can email us [here](mailto:y.mohammad@nec.com)


## Table of Contents

- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [1. Installation](#1-installation)
  - [Using uv (Recommended)](#using-uv-recommended)
  - [Using pip](#using-pip)
- [2. Getting Started: Rename Your Agent](#2-getting-started-rename-your-agent)
  - [VS Code](#vs-code)
  - [PyCharm](#pycharm)
  - [Vim/Neovim (with LSP)](#vimneovim-with-lsp)
  - [Manual Renaming (Any Editor)](#manual-renaming-any-editor)
- [3. Implementing Your Agent](#3-implementing-your-agent)
  - [Example Agents](#example-agents)
- [4. Customizing Your Agent](#4-customizing-your-agent)
  - [Modifying Prompts](#modifying-prompts)
  - [Using Tags in Prompts](#using-tags-in-prompts)
  - [Customizing Example Agents](#customizing-example-agents)
- [5. Usage from the command line](#5-usage-from-the-command-line)
  - [Running a single negotiation](#running-a-single-negotiation)
  - [Running a tournament](#running-a-tournament)
  - [Viewing Development and Submission Info](#viewing-development-and-submission-info)
  - [Viewing Available Prompt Tags](#viewing-available-prompt-tags)
- [6. Development Workflows](#6-development-workflows)
  - [VS Code](#vs-code-1)
  - [Vim/Neovim](#vimneovim)
  - [PyCharm / Other IDEs](#pycharm--other-ides)
- [7. Submission](#7-submission)

## Project Structure

```
.
├── examples/              # Example negotiator implementations
│   ├── adapter.py         # LLM-based adapter that wraps existing negotiators
│   └── nollm.py           # Non-LLM negotiators (BOA and simple SAO)
├── scenarios/             # Negotiation scenarios
│   ├── Amsterdam/
│   ├── Camera/
│   ├── Car/
│   ├── Grocery/
│   ├── ISBTAcquisition/
│   ├── Laptop/
│   └── NiceOrDie/
├── main.py                # CLI application entry point
├── mynegotiator.py        # Your agent implementation (RENAME & EDIT THIS!)
├── pyproject.toml         # Project configuration
└── README.md
```

## 1. Installation

### Using uv (Recommended)

First, install [uv](https://docs.astral.sh/uv/) if you do not have it:

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install the project dependencies (all platforms):

```bash
uv sync
```

To update NegMAS to the latest version (all platforms):

```bash
uv sync --upgrade-package negmas
```

### Using pip

**Linux/macOS:**
```bash
pip install -e .
```

**Windows:**
```cmd
pip install -e .
```

## 2. Getting Started: Rename Your Agent

Before you start developing, rename the agent module and class to match your submission name. This helps identify your agent in tournaments and is required for submission.

**Naming conventions:**
- **Module (file):** `snake_case` (e.g., `awesome.py`, `smart_negotiator.py`)
- **Class:** `TitleCase` (e.g., `AwesomeNegotiator`, `SmartNegotiator`)

### VS Code

1. **Rename the file:**
   - Right-click `mynegotiator.py` in the Explorer → Rename
   - Enter your new name (e.g., `awsome.py`)

2. **Rename the class:**
   - Open the renamed file
   - Click on `MyNegotiator` class name
   - Press `F2` (or right-click → Rename Symbol)
   - Enter your new class name (e.g., `AwesomeNegotiator`)

3. **Update imports in `main.py`:**
   - Open `main.py`
   - Change line 20: `from mynegotiator import MyNegotiator`
   - To: `from awesome import AwesomeNegotiator`
   - Update line 186: `MyNegotiator(...)` → `AwesomeNegotiator(...)`
   - Update line 198: `"mynegotiator.MyNegotiator"` → `"awsome.AwesomeNegotiator"`

### PyCharm

1. **Rename the file:**
   - Right-click `mynegotiator.py` in Project view → Refactor → Rename (or `Shift+F6`)
   - Enter your new name (e.g., `awesome.py`)
   - Check "Search for references" and "Search in comments and strings"

2. **Rename the class:**
   - Open the renamed file
   - Right-click on `MyNegotiator` → Refactor → Rename (or `Shift+F6`)
   - Enter your new class name (e.g., `AwesomeNegotiator`)
   - PyCharm will update all references automatically

3. **Verify imports in `main.py`** are updated correctly

### Vim/Neovim (with LSP)

1. **Rename the file:**
   ```bash
   mv mynegotiator.py awesome.py
   ```

2. **Rename the class (using LSP rename):**
   - Open the file and place cursor on `MyNegotiator`
   - Use your LSP rename command (commonly `<leader>rn` or `:lua vim.lsp.buf.rename()`)
   - Enter the new name (e.g., `AwesomeNegotiator`)

3. **Update imports in `main.py`:**
   - Change `from mynegotiator import MyNegotiator` to `from awesome import AwesomeNegotiator`
   - Update usages of `MyNegotiator` to `AwesomeNegotiator`

### Manual Renaming (Any Editor)

1. **Rename the file:**
   ```bash
   mv mynegotiator.py awesome.py
   ```

2. **Edit the renamed file:**
   - Change `class MyNegotiator` to `class AwesomeNegotiator` (or your chosen name)

3. **Edit `main.py`:**
   - Line 20: Change `from mynegotiator import MyNegotiator` to `from awesome import AwesomeNegotiator`
   - Line 186: Change `MyNegotiator(...)` to `AwesomeNegotiator(...)`
   - Line 198: Change `"mynegotiator.MyNegotiator"` to `"awesome.AwesomeNegotiator"`

4. **Verify the changes:**
   ```bash
   han2026 run
   ```

## 3. Implementing Your Agent

Your agent is implemented in your renamed module file. See the example agents below for different approaches to building agents.

### Example Agents

The `examples/` folder contains example negotiator implementations that demonstrate different approaches to building agents:

#### BolwareBasedLLMNegotiator (`examples/adapter.py`)

An **LLM-based adapter** that wraps existing negotiators to add natural language communication capabilities. This example demonstrates how to use `LLMMetaNegotiator` to enhance any traditional negotiator with LLM-powered decision making:

- **Base Negotiator:** Uses `BoulwareTBNegotiator` as the underlying strategy (a time-based tough negotiator)
- **LLM Enhancement:** The LLM learns from and adapts the base negotiator's behavior
- **Hybrid Approach:** Combines the reliability of traditional strategies with LLM flexibility

This is useful when you want to leverage proven negotiation strategies while adding natural language reasoning.

You can test it with:

```bash
han2026 run --opponent examples.adapter.BolwareBasedLLMNegotiator
```

#### Non-LLM Negotiators (`examples/nollm.py`)

This file contains two traditional (non-LLM) negotiators that don't require an LLM to run:

**BOANeg** - A modular agent using the **BOA (Bidding, Opponent modeling, Acceptance)** architecture:

- **Bidding Strategy:** Uses `TimeBasedOfferingPolicy` - makes concessions based on remaining time
- **Opponent Model:** Uses `GSmithFrequencyModel` - learns opponent preferences from their offers
- **Acceptance Strategy:** Uses `ACNext` - accepts if the offer is better than what we would offer next

```bash
han2026 run --opponent examples.nollm.BOANeg
```

**SimpleNeg** - A minimal agent implemented in a single function, demonstrating the basics:

- **Acceptance:** Accepts any offer with utility > 0.8
- **Offering:** Always proposes the best outcome for itself
- **Natural Text:** Includes simple response messages ("Thank you for this great offer", etc.)

This is a good starting point to understand the negotiation API before moving to more complex architectures.

```bash
han2026 run --opponent examples.nollm.SimpleNeg
```

You can see all available components from negmas using:

```bash
python -c "from negmas.registry import component_registry as CR; print(CR.keys());"
```

> [!NOTE]
> You can base your agent on any supported NegMAS negotiator (For some examples check [this](https://negmas.readthedocs.io/en/latest/negotiators.html) list. Other agents are available through [negmas-negobog](https://autoneg.github.io/negmas-negolog/) and [negmas-geniusweb-bridge](https://autoneg.github.io/negmas-geniusweb-bridge/)). You can explore available negotiators, their behavior, etc in the [NegMAS GUI](https://autoneg.github.io/negmas-app/).


## 4. Customizing Your Agent

### Modifying Prompts

Your agent uses several prompts defined as module-level variables at the top of your agent file. You can customize these to change how the LLM thinks about and approaches negotiation.

#### Available Prompt Variables

In your agent file (e.g., `mynegotiator.py`), you'll find these module-level prompt variables:

- **`SYSTEM_PROMPT`** - Sets the overall behavior, personality, and role of the LLM negotiator
- **`PREFERENCES_PROMPT`** - Sent when preferences are first set at the start of negotiation
- **`PREFERENCES_CHANGED_PROMPT`** - Sent when preferences change during negotiation (rare)
- **`NEGOTIATION_START_PROMPT`** - Sent when negotiation begins, explains the response format
- **`ROUND_PROMPT`** - Sent each negotiation round with current state information

Each prompt can include **tags** (see [Using Tags in Prompts](#using-tags-in-prompts)) that get dynamically replaced with negotiation context.

#### Example: Creating an Aggressive Negotiator

To make your agent more aggressive and less willing to compromise:

```python
SYSTEM_PROMPT = """
You are a TOUGH negotiator who drives HARD bargains. Your primary goal
is to maximize your own utility, and you should be very reluctant to
make concessions. Only accept offers that give you excellent utility.

Be assertive in your text messages to the opponent. Make it clear you
expect favorable terms. Start with your best possible outcomes and
concede slowly and reluctantly only when time is running out.

Always respond in the exact JSON format requested.
"""
```

#### Example: Creating a Cooperative Negotiator

To make your agent more cooperative and focused on mutual benefit:

```python
SYSTEM_PROMPT = """
You are a COOPERATIVE negotiator focused on finding win-win solutions.
While you aim for good utility, you also value reaching agreements that
benefit both parties. Analyze the opponent's preferences when available
and look for outcomes that provide high joint utility.

Be friendly and collaborative in your text messages. Explain your
reasoning and show willingness to compromise when it makes sense.

Always respond in the exact JSON format requested.
"""
```

#### Example: Adding Opponent Modeling to Negotiation Start

You can enhance the `NEGOTIATION_START_PROMPT` to encourage the LLM to model the opponent:

```python
NEGOTIATION_START_PROMPT = """
# Negotiation Started

The negotiation has now started. For each round, you should:

1. **Model your opponent**: Track which outcomes they offer and accept
   to infer their preferences. Use {{history:text(k=5)}} to see recent moves.
2. **Analyze offers**: When you receive an offer, check its utility for you
   using {{utility:text(outcome={{opponent-last-offer}})}}
3. **Make strategic decisions**: Choose to ACCEPT, REJECT (with counter-offer), or END
4. **Communicate effectively**: Provide persuasive text that advances your position

Respond in this JSON format for each decision:
```json
{
    "response_type": "accept" | "reject" | "end" | "wait",
    "outcome": [value1, value2, ...] | null,
    "text": "optional persuasive message to send to your opponent",
    "reasoning": "brief explanation of your decision (not sent to opponent)"
}
```

Ready to begin!
"""
```

### Using Tags in Prompts

Tags allow you to dynamically insert negotiation context into prompts. They are written as `{{tag-name}}` or `{{tag-name:format(param=value)}}`.

#### Common Tags and Examples

To see all available tags, run:
```bash
han2026 tags
```

Here are some frequently used tags:

**Outcome Space Tags:**
- `{{outcome-space:json}}` - Get the full outcome space in JSON format
- `{{outcome-space:text}}` - Get human-readable outcome space description
- `{{n-outcomes}}` - Number of possible outcomes

**Utility Tags:**
- `{{utility:text(outcome={{opponent-last-offer}})}}` - Compute utility of opponent's last offer
- `{{utility-function:text}}` - Your utility function description
- `{{reserved-value}}` - Your walk-away utility value
- `{{opponent-utility-function:text}}` - Opponent's utility (if available)

**History Tags:**
- `{{history:text}}` - Full negotiation history
- `{{history:text(k=5)}}` - Last 5 negotiation steps
- `{{opponent-last-offer}}` - Opponent's most recent offer
- `{{my-last-offer}}` - Your most recent offer

**Context Tags:**
- `{{nmi:text}}` - Negotiation mechanism information (time limit, steps, etc.)
- `{{step}}` - Current negotiation step number
- `{{relative-time}}` - How much time has elapsed (0.0 to 1.0)
- `{{running}}` - Whether negotiation is still active

#### Example: Rich Round Prompt with Multiple Tags

```python
ROUND_PROMPT = """
# Round {{step}}

**Progress**: Step {{step}} | Time: {{relative-time:.1%}} | Running: {{running}}

## Current Situation
{{history:text(k=3)}}

## Opponent's Last Offer
{{opponent-last-offer}}

**Utility for you**: {{utility:text(outcome={{opponent-last-offer}})}}

## Your Last Offer
{{my-last-offer}}

## Analysis
- Your reserved value (walk-away point): {{reserved-value}}
- Total possible outcomes: {{n-outcomes}}

What is your decision? Remember to maximize your utility while considering
the time pressure and opponent's apparent preferences.

Respond with JSON.
"""
```

### Customizing Example Agents

#### Adapter Example (`examples/adapter.py`)

The adapter wraps a traditional negotiator with LLM capabilities. You can customize:

**1. Change the Base Negotiator:**

Replace `BoulwareTBNegotiator` (tough negotiator) with a different strategy:

```python
from negmas.sao import ConcederTBNegotiator  # More willing to concede

class CooperativeLLMNegotiator(LLMMetaNegotiator):
    def __init__(self, **kwargs):
        super().__init__(
            negotiator=ConcederTBNegotiator(),  # Changed from BoulwareTBNegotiator
            system_prompt=SYSTEM_PROMPT,
            **kwargs
        )
```

**2. Modify the System Prompt:**

The `SYSTEM_PROMPT` in `adapter.py` controls how the LLM generates text. Customize it to change the communication style:

```python
SYSTEM_PROMPT = """
You are assisting in automated negotiation by generating natural language
messages. Be BRIEF and DIRECT - keep messages under 20 words when possible.

Available information:
- {{outcome-space:text}}
- {{history:text(k=3)}}

Generate concise, persuasive text based on the negotiation context.
"""
```

**3. Adjust LLM Parameters:**

```python
class MyCustomAdapter(LLMMetaNegotiator):
    def __init__(self, **kwargs):
        super().__init__(
            negotiator=BoulwareTBNegotiator(),
            system_prompt=SYSTEM_PROMPT,
            model="llama3.2",           # Different model
            temperature=0.9,            # More creative responses
            max_tokens=512,             # Shorter responses
            **kwargs
        )
```

#### Non-LLM Examples (`examples/nollm.py`)

**BOANeg** uses modular components you can swap:

```python
from negmas.sao import AspirationNegotiator, GaussianAcceptanceStrategy

# More flexible bidding strategy
bidding_strategy = AspirationNegotiator(max_aspiration=0.9, aspiration_type='linear')

# Different acceptance strategy
acceptance_strategy = GaussianAcceptanceStrategy()

class MyBOANeg(SAONegotiator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_capabilities(
            offering=bidding_strategy,
            acceptance=acceptance_strategy,
            opponent_model=GSmithFrequencyModel()
        )
```

**SimpleNeg** can be modified to be more strategic:

```python
def respond(state, offer):
    my_utility = self.ufun(offer) if offer else 0.0
    
    # More sophisticated acceptance threshold
    time_pressure = state.relative_time
    threshold = 0.7 + (0.2 * time_pressure)  # Accept lower offers as time runs out
    
    if my_utility >= threshold:
        return SAOResponse(ResponseType.ACCEPT_OFFER, offer)
    
    # Find best counter-offer
    outcomes = self.nmi.outcome_space.enumerate()
    best = max(outcomes, key=lambda o: self.ufun(o))
    
    return SAOResponse(
        ResponseType.REJECT_OFFER,
        best,
        f"I propose this alternative (utility for me: {self.ufun(best):.2f})"
    )
```

For detailed tag documentation, use:
```bash
han2026 tags <tag-name>
```

## 5. Usage from the command line

> **Note:** All commands below work on Linux, macOS, and Windows. On Windows, use Command Prompt, PowerShell, or Windows Terminal.

### Running a single negotiation

To run a single negotiation:

```bash
han2026 run
```

This will run your agent against a random opponent on a random scenario and report:
- **Advantage:** utility - reserved-value
- **Deception:** How well you confuse your opponent's model of you
- **Score:** The final HAN 2026 score

#### Run command options

| Option | Description |
|--------|-------------|
| `--scenario TEXT` | Scenario name to use (default: random from scenarios folder) |
| `--generate-scenario` | Generate a random scenario instead of loading one |
| `--rational-fraction FLOAT` | Fraction of rational outcomes in generated scenarios (0.0-1.0, default: 1.0) |
| `--opponent TEXT` | Opponent class to negotiate against (default: random) |
| `--verbose` | Show full negotiation trace with utilities |
| `--plot / --no-plot` | Plot the negotiation trace (default: plot) |

Examples:
```bash
# Run with a specific scenario
han2026 run --scenario Camera

# Run with a generated scenario
han2026 run --generate-scenario

# Run against a specific opponent (Any negmas/genius agent can be used this way)
han2026 run --opponent negmas.sao.BoulwareTBNegotiator


# Run against a specific opponent (Any example can be used this way)
han2026 run --opponent examples.boa.BOANeg

# Run with verbose output and no plot
han2026 run --verbose --no-plot
```

### Running a tournament

To run a complete tournament with all default competitors:

```bash
han2026 tournament
```

This will run your agent against multiple opponents across all scenarios and report the final scores.

#### Tournament command options

| Option | Description |
|--------|-------------|
| `--name TEXT` | Tournament name (default: auto-generated) |
| `--competitor TEXT` | Competitor classes to include (can be repeated, default: built-in competitors) |
| `--scenario TEXT` | Scenario names or paths (can be repeated, use 'all' for all scenarios) |
| `--generate-scenarios N` | Generate N random scenarios |
| `--rational-fraction FLOAT` | Fraction of rational outcomes in generated scenarios (0.0-1.0) |
| `--verbosity INT` | Verbosity level 0-5 (default: 0 = silent) |
| `--parallel` | Run tournament in parallel mode using all cores |

Examples:
```bash
# Run tournament on specific scenarios
han2026 tournament --scenario Camera --scenario Car

# Run tournament with generated scenarios
han2026 tournament --generate-scenarios 10

# Run tournament in parallel with verbose output
han2026 tournament --parallel --verbosity 1

# Run tournament with custom competitors
han2026 tournament --competitor mynegotiator.MyNegotiator --competitor examples.boa.BOANeg
```

### Viewing Development and Submission Info

To view development workflows and submission instructions in your terminal:

```bash
han2026 info
```

### Viewing Available Prompt Tags

To see all available tags for customizing LLM prompts:

```bash
han2026 tags
```

To get detailed documentation for a specific tag:

```bash
han2026 tags utility
han2026 tags outcome-space
```

Tags can be used in custom prompts to dynamically insert negotiation context such as outcome space, utilities, negotiation history, and opponent information.

## 6. Development Workflows

### VS Code

1. Open the project folder in VS Code
2. Install the recommended Python extension
3. Select the Python interpreter from `.venv`:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from `.venv/bin/python` (Linux/macOS) or `.venv\Scripts\python.exe` (Windows)
4. Edit your agent file (renamed from `mynegotiator.py`) to implement your agent
5. Run tests with `pytest` in the integrated terminal
6. Run your agent with `han2026 run`

### Vim/Neovim

1. Ensure you have a Python LSP configured (e.g., pyright, pylsp)
2. Activate the virtual environment or use `uv run` prefix for commands
3. Edit your agent file (renamed from `mynegotiator.py`) to implement your agent
4. Run commands from the terminal:
   ```bash
   han2026 run
   pytest
   ```

### PyCharm / Other IDEs

1. Open the project folder
2. Configure the Python interpreter to use `.venv`:
   - Go to Settings/Preferences > Project > Python Interpreter
   - Add the interpreter from `.venv/bin/python` (Linux/macOS) or `.venv\Scripts\python.exe` (Windows)
3. Edit your agent file (renamed from `mynegotiator.py`) to implement your agent
4. Use the built-in terminal to run:
   ```bash
   han2026 run
   pytest
   ```

## 7. Submission

<!-- SUBMISSION_START -->
To submit your agent to the HAN 2026 competition:

1. Ensure your renamed your agent and followed the instruction for development and have a runnable agent. To test that you have a runnable agent, use:

  ```bash
  han2026 run
  ```

and

  ```bash
  han2026 tournament
  ```

2. Test your agent locally using `han2026 run` and `han2026 tournament`
3. Add any extra dependencies you need for your agent in requirements.txt. Try to always use the most recent version of each library to maximize the re-usability of your agent in the future.
4. Zip the code for your agent (no need to include examples, scenarios, report, tests, README.md, main.py, pyproject.toml, uv.lock) in your submission:

   **Using the provided scripts (recommended):**

   Linux/macOS:
   ```bash
   ./make_submission.sh
   ```

   Windows:
   ```cmd
   make_submission.bat
   ```

   **Or manually:**

   Linux/macOS:
   ```bash
   zip -r submission.zip . -x "examples/*" -x "scenarios/*" -x "report/*" -x "tests/*" -x "README.md" -x "main.py" -x "pyproject.toml" -x "uv.lock" -x ".git/*" -x ".venv/*" -x "__pycache__/*" -x "*.pyc" -x ".ruff_cache/*" -x ".pytest_cache/*"
   ```

   Windows (PowerShell):
   ```powershell
   Get-ChildItem -Exclude examples, scenarios, report, tests, README.md, main.py, pyproject.toml, uv.lock, .git, .venv, __pycache__, .ruff_cache, .pytest_cache | Compress-Archive -DestinationPath submission.zip -Force
   ```

   Windows (Command Prompt with tar):
   ```cmd
   tar -a -cf submission.zip --exclude=examples --exclude=scenarios --exclude=report --exclude=tests --exclude=README.md --exclude=main.py --exclude=pyproject.toml --exclude=uv.lock --exclude=.git --exclude=.venv --exclude=__pycache__ --exclude=.ruff_cache --exclude=.pytest_cache .
   ```

5. Submit your agent following the competition guidelines at [HAN 2026 Competition Page](https://anac.cs.brown.edu/han)

   5.1. [First time] Register for the competition [here](https://anac.cs.brown.edu/register)

   5.2. Login for the submission site [here](https://anac.cs.brown.edu/register)

   5.3. Go to your home page "Your Home" and choose "Submissions"

   5.4. Under "HAN", click "New Agent" and fill the form. We will assume that your main agent class is called `AwsomeNegotiator` implemented in a file called `awsome.py` at the root of this folder:

     - Agent Name: Awsome Negotiator
     - Agent Alias: Awsome Negotiator
     - Agent Module: awsome
     - Agent Class: AwsomeNegotiator
     - Dependencies: <any dependencies you had to `pip install` or `uv add` yourself in a semicolon-separated list, no spaces>
     - Code: submission.zip
     - Requirements File: requirements.txt
     - Report: <upload your report pdf>. This is only required for the final submission but it is safe to submit drafts of it at any time. No one will read them before the final submission deadline.

   > [!NOTE]
   > If you need to use data files (e.g. trained models, any files that your agent READs in real time for successful operation), make sure they are included in the zipped submission file and read this FAQ entry: [Accessing Data Files](https://scml.readthedocs.io/en/latest/faq.html#how-can-i-access-a-data-file-in-my-package). This is written for the SCML league but the process is EXACTLY the same.

You can submit your agent as many times as you want until the competition deadline. Please submit early and frequently. When you submit your agent, we run tests on it and you will get feedback if it is failing in the competition. Moreover, we keep a running leaderboard [here](https://anac.cs.brown.edu/leaderboard) which allows you to judge different improvements you make against your real opponents in the competition.


<!-- SUBMISSION_END -->
