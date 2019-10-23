#                 GLWT(Good Luck With That) Public License
#                   Copyright (c) Everyone, except Author
#
#  Everyone is permitted to copy, distribute, modify, merge, sell, publish,
#  sublicense or whatever they want with this software but at their OWN RISK.
#
#                              Preamble
#
#  The author has absolutely no clue what the code in this project does.
#  It might just work or not, there is no third option.
#
#
#                  GOOD LUCK WITH THAT PUBLIC LICENSE
#     TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION, AND MODIFICATION
#
#    0. You just DO WHATEVER YOU WANT TO as long as you NEVER LEAVE A
#  TRACE TO TRACK THE AUTHOR of the original product to blame for or hold
#  responsible.
#
#  IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#
#  Good luck and Godspeed.

import pygame
import colors

# Stolen from the internet to create buttons easily
# https://www.youtube.com/watch?v=4_9twnEduFA


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, colors.black)
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
