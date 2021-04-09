import processing.core.*;

public class ConwayLife extends PApplet {

    int s1x = 30;
    int s1y = 30;
    int s2 = 20;

    char[][] gen = {};
    char[][] next_gen = {};
    boolean[][] clicks = {};

    int zero = 50;
    int one = 250;
    int cell_stroke = 60;
    int erasing = 0;
    int adding = 1;
    int changing = 2;

    boolean kClick = false;
    int population = 0;
    int generation = 0;
    int keyDelay = 0;
    int maxKeyDelay = 40;
    int maxFrames = 40;
    int mouseMode = adding;

    public void setup() {
        gen = new char[s1x][s1y];
        next_gen = new char[s1x][s1y];
        clicks = new boolean[s1x][s1y];

        for (int x = 0; x < s1x; x++) {
            for (int y = 0; y < s1y; y++) {
                if (gen[x][y] == one) {
                    population += 1;
                }
            }
        }

        size(s1x * s2 + 1, s1y * s2 + 1);
        show();
    }

    public char cell(int x, int y) {
        char c = 0;
        if ((x >= 0) && (x < s1x)) {
            if ((y >= 0) && (y < s1y)) {
                c = gen[x][y];
            }
        }
        return c;
    }

    public int neighbours(int x, int y) {
        int n = -cell(x, y);
        for (int ix = 0; ix < 3; ix++) {
            for (int iy = 0; iy < 3; iy++) {
                n += cell(x + ix - 1, y + iy - 1);
            }
        }
        return n;
    }

    public void show() {
        for (int x = 0; x < s1x; x++) {
            for (int y = 0; y < s1y; y++) {
                if (gen[x][y] == 0) {
                    fill(zero);
                    stroke(cell_stroke);
                } else {
                    fill(one);
                    stroke(cell_stroke);
                }
                rect(s2 * x, s2 * y, s2, s2);
            }
        }
        for (int x = 0; x < s1x; x++) {
            for (int y = 0; y < s1y; y++) {
                fill(128);
                textAlign(CENTER, CENTER);
                text(neighbours(x, y), (int)(s2 * (x + 0.5)), (int)(s2 * (y + 0.5)));
            }
        }
    }

    public void mouseDraw() {
        if (mousePressed) {
            int x = mouseX / s2;
            int y = mouseY / s2;
            clicks[x][y] = true;
            if (mouseMode == changing) {
                if (gen[x][y] == 0) {
                    mouseMode = adding;
                } else {
                    mouseMode = erasing;
                }
            }
            if (mouseMode == adding) {
                next_gen[x][y] = 1;
                population += 1;
            } else {
                next_gen[x][y] = 0;
                population -= 1;
            }
        }
        for (int x = 0; x < s1x; x++) {
            for (int y = 0; y < s1y; y++) {
                gen[x][y] = next_gen[x][y];
            }
        }
        show();
    }

    public void draw() {
        mouseDraw();
        show();
        if (!mousePressed) {
            for (int x = 0; x < s1x; x++) {
                for (int y = 0; y < s1y; y++) {
                    if (clicks[x][y]) {
                        clicks[x][y] = false;
                    }
                }
            }
            mouseMode = changing;
        }

        if (!keyPressed) {
            kClick = false;
            keyDelay = 0;
        } else {
            keyDelay += 1;
        }
        if (keyDelay > maxKeyDelay) {
            keyDelay = maxKeyDelay;
        }
        if (keyPressed && ((!kClick) || (keyDelay > maxKeyDelay - 1))) {
            kClick = true;
            if (keyDelay > maxKeyDelay - 1) {
                keyDelay = maxFrames;
            }
            generation += 1;
            for (int x = 0; x < s1x; x++) {
                for (int y = 0; y < s1y; y++) {
                    int nCount = neighbours(x, y);
                    next_gen[x][y] = gen[x][y];
                    if (nCount == 3) {
                        next_gen[x][y] = 1;
                    } else if ((nCount < 2) || (nCount > 3)) {
                        next_gen[x][y] = 0;
                    }
                    if ((next_gen[x][y] == 0) && (nCount == 3)) {
                        population += 1;
                    } else if ((next_gen[x][y] == 1) && ((nCount < 2) || (nCount > 3))) {
                        population -= 1;
                    }
                }
            }
        }

        for (int x = 0; x < s1x; x++) {
            for (int y = 0; y < s1y; y++) {
                gen[x][y] = next_gen[x][y];
            }
        }
    }

    public static void main(String[] args) {
        PApplet.main(new String[] {"ConwayLife"});
    }

}
