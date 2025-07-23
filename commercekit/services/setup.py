import subprocess
import os
import typer

class ThemeSetupService:
    def run_command(self, cmd, suppress_output=True):
        if suppress_output:
            result = subprocess.run(
                cmd, shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                executable="/bin/bash"
            )
        else:
            result = subprocess.run(cmd, shell=True, executable="/bin/bash")
        if result.returncode != 0:
            typer.secho(f"❌ Command failed: {cmd}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

    def run_nvm_command(self, cmd, suppress_output=True):
        nvm_init = (
            'export NVM_DIR="$HOME/.nvm" && '
            '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && '
            f'{cmd}'
        )
        self.run_command(nvm_init, suppress_output=suppress_output)

    def is_nvm_installed(self):
        try:
            result = subprocess.run(
                ['nvm', '--version'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                executable="/bin/bash"
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def install_node_with_nvm(self):
        if not self.is_nvm_installed():
            typer.secho("Installing nvm (Node Version Manager)...", fg=typer.colors.YELLOW)
            self.run_command('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash')
            typer.secho("✅ nvm installed successfully.", fg=typer.colors.GREEN)
        else:
            typer.secho("nvm is already installed, skipping installation.", fg=typer.colors.CYAN)

        typer.secho("Installing latest Node.js version via nvm...", fg=typer.colors.YELLOW)
        self.run_nvm_command('nvm install node')
        typer.secho("✅ Node.js installed and activated.", fg=typer.colors.GREEN)

    def get_version(self, cmd):
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            executable="/bin/bash",
            text=True,
            env={**os.environ, "NVM_DIR": os.path.expanduser("~/.nvm")}
        )
        if result.returncode != 0:
            return "unknown"
        return result.stdout.strip()

    def install_shopify_cli(self):
        typer.secho("Installing latest Shopify CLI via npm...", fg=typer.colors.YELLOW)
        try:
            self.run_nvm_command('npm install -g @shopify/cli@latest', suppress_output=True)
            typer.secho("✅ Shopify CLI installed successfully.", fg=typer.colors.GREEN)
        except typer.Exit:
            typer.secho("❌ Failed to install Shopify CLI.", fg=typer.colors.RED)
            raise

    def print_versions_box(self):
        node_version = self.get_version('node -v')
        npm_version = self.get_version('npm -v')
        shopify_version = self.get_version('shopify version')

        box_width = 42
        border = "─" * box_width
        line_color = typer.colors.BRIGHT_YELLOW  # Oranje
        text_color = typer.colors.WHITE  # Witte tekst

        typer.secho(f"┌{border}┐", fg=line_color)
        typer.secho(f"│{'Installed Versions':^{box_width}}│", fg=text_color, bold=True)
        typer.secho(f"├{border}┤", fg=line_color)
        typer.secho(f"│ Node.js:      {node_version:<{box_width - 13}}│", fg=text_color)
        typer.secho(f"│ npm:         {npm_version:<{box_width - 13}}│", fg=text_color)
        typer.secho(f"│ Shopify CLI: {shopify_version:<{box_width - 15}}│", fg=text_color)
        typer.secho(f"└{border}┘", fg=line_color)

    def setup_theme_cli(self, platform: str):
        typer.secho(f"Setting up theme development for platform: {platform}", fg=typer.colors.BRIGHT_YELLOW, bold=True)

        if platform.lower() == "shopify":
            typer.secho("Running Shopify specific setup...", fg=typer.colors.BRIGHT_YELLOW)
            self.install_node_with_nvm()
            self.install_shopify_cli()
            self.print_versions_box()
            typer.secho("🎉 Setup complete! You're ready to develop.", fg=typer.colors.BRIGHT_YELLOW, bold=True)
        elif platform.lower() == "lightspeed":
            typer.secho("Running Lightspeed specific setup...", fg=typer.colors.BRIGHT_YELLOW)
            # TODO: Lightspeed setup
        else:
            typer.secho(f"No setup steps defined for platform '{platform}'", fg=typer.colors.RED)
