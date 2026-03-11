import flet as ft

def main(page: ft.Page):
    page.title = "AQMA Dashboard"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # Komponen UI
    header = ft.Text("AQMA MONITORING SYSTEM", size=24, weight="bold", color="blue")
    status_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.SHIELD_OUTLINED, color="blue"),
                        title=ft.Text("System Status"),
                        subtitle=ft.Text("All systems operational", color="green"),
                    ),
                    ft.Row(
                        [ft.Text("Efficiency: 98%", size=12), ft.Text("Uptime: 00:01:24", size=12)],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                ],
                spacing=10,
            ),
            padding=10,
        )
    )

    log_box = ft.Column(spacing=5)
    
    def add_log(message, color="white"):
        log_box.controls.append(ft.Text(f"> {message}", color=color, size=12, font_family="monospace"))
        page.update()

    def start_click(e):
        btn_start.disabled = True
        add_log("Initializing AQMA protocols...", "blue")
        add_log("Scanning quality parameters...", "yellow")
        add_log("AQMA ACTIVE - Monitoring started.", "green")
        page.update()

    btn_start = ft.ElevatedButton("ACTIVATE AQMA", icon=ft.icons.PLAY_ARROW, on_click=start_click, width=300)

    # Susunan Tampilan
    page.add(
        header,
        ft.Text("Pembuat: JB", size=16, color="grey"),
        ft.Divider(height=20),
        status_card,
        ft.Container(height=20),
        btn_start,
        ft.Text("Activity Logs:", size=14, weight="bold"),
        ft.Container(
            content=log_box,
            bgcolor=ft.colors.BLACK,
            padding=10,
            border_radius=10,
            expand=True,
            height=200
        )
    )

# Ini akan memaksa AQMA membuka jalur web di port 8080
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)

