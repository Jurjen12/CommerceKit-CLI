import typer

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

if __name__ == "__main__":
    app()
