import tkinter as tk

class ZoomingCanvas(tk.Canvas):
    def __init__(self, parent, xsc, ysc, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.create_polygon(0.0, 0.0, xsc, 0.0, 0.0, ysc, 
                            state=tk.HIDDEN, tags='_coords')
        self._screg_padx0 = 1
        self._screg_pady0 = 1
        self._screg_padx1 = 2
        self._screg_pady1 = 2
        self._cx0 = 0
        self._cy0 = 0
        self._cxsc = xsc
        self._cysc = ysc
        self.bind("<Button-4>", self.zoomIn)
        self.bind("<Button-5>", self.zoomOut)

    def _getPaddedBB(self):
        bb = list(self.bbox('all'))
        bb[0] -= self._screg_padx0
        bb[1] -= self._screg_pady0
        bb[2] += self._screg_padx1
        bb[3] += self._screg_pady1
        return bb

    def _updateScrollregion(self):
        self.configure(scrollregion=self._getPaddedBB())

    def _updateTranslation(self):
        coords = self.coords('_coords')
        assert len(coords) == 6
        self._cx0 = coords[0]
        self._cy0 = coords[1]
        self._cxsc = coords[2] - coords[0]
        self._cysc = coords[5] - coords[1]

    def stat2canx(self, x):
        return self._cx0 + self._cxsc * x

    def stat2cany(self, y):
        return self._cy0 + self._cysc * y

    def zoom(self, scale=None, cx=None, cy=None):
        (scx0, scy0, scx1, scy1) = self._getPaddedBB()
        (xv0, xv1) = self.xview()
        (yv0, yv1) = self.yview()
        cw = float(self.cget('width'))
        ch = float(self.cget('height'))
        if scale is None:
            scx = cw / (1e-15 + scx1 - scx0)
            scy = ch / (1e-15 + scy1 - scy0)
            scale = min(scx, scy)
        if cx is None:
            cx = ((xv0 + xv1) * scx1 + (2 - xv1 - xv0) * scx0) / 2.0
        if cy is None:
            cy = ((yv0 + yv1) * scy1 + (2 - yv1 - yv0) * scy0) / 2.0
        self.scale('all', cx, cy, scale, scale)
        self._updateScrollregion()
        self._updateTranslation()

    def zoomIn(self, event=None):
        if event:
            self.zoom(1.25, self.canvasx(event.x), self.canvasy(event.y))
        else:
            self.zoom(1.25)

    def zoomOut(self, event=None):
        if event:
            self.zoom(0.8, self.canvasx(event.x), self.canvasy(event.y))
        else:
            self.zoom(0.8)


class TrackView(ZoomingCanvas):
    def __init__(self, parent, track, **kwargs):
        kwargs.setdefault('width', 1500)
        kwargs.setdefault('height', 1100)
        ZoomingCanvas.__init__(self, parent, 10, -10, 
                               background='#b2b2b2', **kwargs)

        self.create_text(650, -350, text="Circuito VectorRace", fill="black", font=('Ubuntu 40'))

        (xmin, ymin, xmax, ymax) = track.bbox()
        for x in range(xmin, xmax+1):
            cx = self.stat2canx(x)
            cy0 = self.stat2cany(ymin)
            cy1 = self.stat2cany(ymax)
            self.create_line(cx, cy0, cx, cy1, fill='#ddd', width=25, tags='grid')
        for y in range(ymin, ymax+1):
            cx0 = self.stat2canx(xmin)
            cx1 = self.stat2canx(xmax)
            cy = self.stat2cany(y)
            self.create_line(cx0, cy, cx1, cy, fill='#ddd', width=25, tags='grid')

        for l in track.barriers:
            self.create_line(self.stat2canx(l.p0.x), self.stat2cany(l.p0.y), 
                             self.stat2canx(l.p1.x), self.stat2cany(l.p1.y), 
                             fill='black', width=25, capstyle=tk.PROJECTING, 
                             tags='barrier')

        for l in track.solution1:
            self.create_line(self.stat2canx(l.p0.x), self.stat2cany(l.p0.y),
            self.stat2canx(l.p1.x), self.stat2cany(l.p1.y),
            fill='yellow', width=20, capstyle=tk.PROJECTING,
            tags='solution')

        for l in track.solution2:
            self.create_line(self.stat2canx(l.p0.x), self.stat2cany(l.p0.y),
            self.stat2canx(l.p1.x), self.stat2cany(l.p1.y),
            fill='blue', width=10, capstyle=tk.PROJECTING,
            tags='solution')

        for l in track.checks:
            cx = self.stat2canx(l.x)
            cy = self.stat2cany(l.y)
            self.create_rectangle(cx-2, cy-2, cx+2, cy+2,
                         outline = "purple", fill = "purple", tags='checks')
        
        self.create_text(650, -150, text="Verde -> Partida\nVermelho -> Chegada\nRoxo -> Checkpoint", fill="black", font=('Ubuntu 20'))

        if track.solution1 != []:
            if track.alg1 == 1:
                tmp_alg = "DFS"
            elif track.alg1 == 2:
                tmp_alg = "BFS"
            elif track.alg1 == 3:
                 tmp_alg = "A*"
            elif track.alg1 == 4:
                 tmp_alg = "Greedy"
            tmp_txt = "Amarelo -> Jogador 1" + " (" + tmp_alg + ", custo -> " + str(track.custo1) + ")"
            self.create_text(650, -100, text=tmp_txt, fill="black", font=('Ubuntu 20'))

        if track.solution2 != []:
            if track.alg2 == 1:
                tmp_alg = "DFS"
            elif track.alg2 == 2:
                tmp_alg = "BFS"
            elif track.alg2 == 3:
                 tmp_alg = "A*"
            elif track.alg2 == 4:
                 tmp_alg = "Greedy"
            tmp_txt = "Azul -> Jogador 2" + " (" + tmp_alg + ", custo -> " + str(track.custo2) + ")"
            self.create_text(650, -80, text=tmp_txt, fill="black", font=('Ubuntu 20'))

        for c in track.colisoes:
             cx = self.stat2canx(c.x)
             cy = self.stat2cany(c.y)
             self.create_rectangle(cx-4, cy-4, cx+4, cy+4, outline = "purple", fill = "purple", tags='collision')

        for s in track.start:	
             cx = self.stat2canx(s.x)
             cy = self.stat2cany(s.y)
             self.create_rectangle(cx-4, cy-4, cx+4, cy+4, 
                         outline = "red", fill = "red", tags='start')
        cx = self.stat2canx(track.finish.x)
        cy = self.stat2cany(track.finish.y)
        self.create_rectangle(cx-4, cy-4, cx+4, cy+4, 
                         outline = "#0c0", fill='#0c0', tags='finish')

        self.zoom()

    def drawPath(self, path, fill='blue', width=3, capstyle=tk.ROUND, tags=[]):
        coords = []
        for p in path:
            coords.extend((self.stat2canx(p.x),self.stat2cany(p.y)))
        tags.append('path')
        self.create_line(coords, fill=fill, width=width, capstyle=capstyle, 
                         tags=tags)
