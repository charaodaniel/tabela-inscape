import inkex
from lxml import etree

class CreateTables(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--linhas", type=int, default=2, help="Número de linhas")
        pars.add_argument("--colunas", type=int, default=2, help="Número de colunas")
        pars.add_argument("--cell_width", type=int, default=100, help="Largura da célula")
        pars.add_argument("--cell_height", type=int, default=50, help="Altura da célula")
        pars.add_argument("--stroke_width", type=float, default=1.0, help="Espessura da borda")
        pars.add_argument("--stroke_color", type=str, default="#000000", help="Cor da borda")
        pars.add_argument("--fill_color", type=str, default="#ffffff", help="Cor de preenchimento")

    def effect(self):
        num_linhas = self.options.linhas
        num_colunas = self.options.colunas
        cell_width = self.options.cell_width
        cell_height = self.options.cell_height
        stroke_width = self.options.stroke_width
        stroke_color = self.options.stroke_color
        fill_color = self.options.fill_color

        # Criar tabela
        for i in range(num_linhas):
            for j in range(num_colunas):
                x = j * cell_width
                y = i * cell_height
                rect = etree.Element(inkex.addNS('rect', 'svg'))
                rect.set('x', str(x))
                rect.set('y', str(y))
                rect.set('width', str(cell_width))
                rect.set('height', str(cell_height))
                rect.set('style', f"fill:{fill_color};stroke:{stroke_color};stroke-width:{stroke_width}px")
                self.svg.get_current_layer().append(rect)

if __name__ == '__main__':
    CreateTables().run()
