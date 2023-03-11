from random import shuffle
import typer
from rich import print as _print
from _get_questions import get_questions

app = typer.Typer(name='QUIZ APP')
CHOICES = {'A': 0, 'B': 1, 'C': 2, 'D': 3}


@app.command()
def main():
    score = 0
    tries = 0
    playing = True
    _print('*' * 23 + '\n[bold green]Welcome to the QUIZ APP!!![/bold green]\n' + '*' * 23)
    limit = typer.prompt('How many questions do you want to answer?', default=5, type=int)
    while playing:
        questions = get_questions(limit)
        for i in questions:
            _print(f'[bold blue]{i.question}[/bold blue]')
            choices = i.incorrect + [i.correct]
            shuffle(choices)
            _print(f'[bold red]A)[/bold red] [yellow]{choices[0]}[/yellow]')
            _print(f'[bold red]B)[/bold red] [yellow]{choices[1]}[/yellow]')
            _print(f'[bold red]C)[/bold red] [yellow]{choices[2]}[/yellow]')
            _print(f'[bold red]D)[/bold red] [yellow]{choices[3]}[/yellow]')
            chosen = typer.prompt('What\'s your answer?', type=str, default='A').upper()
            chosen = choices[CHOICES.get(chosen, 'A')]
            if chosen == i.correct:
                _print('[bold green]That was a correct answer!!![/bold green]')
                score += 1
            else:
                _print('[bold green]That was a wrong answer :( [/bold green]')
            tries += 1
            _print(f'Score: {score}/{tries}...\n')

        playing = typer.prompt('Do you want to play again?', default=True, type=bool, confirmation_prompt=True)


if __name__ == '__main__':
    app()
