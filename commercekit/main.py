
# main.py
import typer
import questionary
from commercekit.services.setup import ThemeSetupService

app = typer.Typer(help="CommerceKit CLI - E-commerce developer tooling")
integration_app = typer.Typer(help="Manage integrations")
theme_dev = typer.Typer(help="Theme development commands")

app.add_typer(integration_app, name="integration")
app.add_typer(theme_dev, name="theme-dev")

@integration_app.command("app-template")
def integration_app_template():
    typer.echo("Generating integration app template...")


@integration_app.command("app-docker-template")
def integration_app_docker_template():
    typer.echo("Generating integration app Docker template...")


@theme_dev.command("lightspeed")
def theme_dev_lightspeed():
    typer.echo("Setting up Lightspeed theme development environment...")


@theme_dev.command("shopify")
def theme_dev_shopify():
    typer.echo("Setting up Shopify theme development environment...")

@theme_dev.command("setup")
def theme_dev_setup():
    platform = questionary.select(
        "Choose a platform to set up:",
        choices=["lightspeed", "shopify"]
    ).ask()

    if not platform:
        typer.echo("Setup cancelled.")
        raise typer.Exit()

    service = ThemeSetupService()
    service.setup_theme_cli(platform)


if __name__ == "__main__":
    app()
