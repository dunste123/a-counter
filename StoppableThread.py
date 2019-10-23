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

import threading

# Create a thread that you can stop with the stop function
# https://stackoverflow.com/a/325528/4807235


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super(StoppableThread, self).__init__(group=group, target=target, name=name, args=args,
                                              kwargs=kwargs, daemon=daemon)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
