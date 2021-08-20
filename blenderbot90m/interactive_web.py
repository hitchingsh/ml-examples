#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Talk with a model using a web UI.

## Examples

```shell
parlai interactive_web -mf "zoo:tutorial_transformer_generator/model"
```
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
from parlai.scripts.interactive import setup_args
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from typing import Dict, Any
from parlai.core.script import ParlaiScript, register_script
import parlai.utils.logging as logging

import json
import time
import re

HOST_NAME = '0.0.0.0'
PORT = 8080

SHARED: Dict[Any, Any] = {}
STYLE_SHEET = "https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.3.1/js/all.js"
WEB_HTML = """
<html>
    <link rel="stylesheet" href={} />
    <script defer src={}></script>
    <head><title>BlenderBot Demo</title></head>
    <body>
        <div class="columns" style="height: 100%">
            <div class="column is-three-fifths is-offset-one-fifth">
              <section class="hero is-info is-large has-background-light has-text-grey-dark" style="height: 100%">
                <div id="parent" class="hero-body" style="overflow: auto; height: calc(100% - 76px); padding-top: 1em; padding-bottom: 0;">
                    <article class="media">
                      <div class="media-content">
                        <div class="content">
                          <p>
                            <strong>Hamilton's BlenderBot Chat Demo</strong>
                            <br>Send messages to have a conversation with this ParlAI BlenderBot
                            <br>demo by hamilton@imagical.co
                            <br>Please wait for the Blenderbot to load in and show its first message before you start chatting, which can take 15 seconds...
                          </p>
                        </div>
                      </div>
                    </article>
                </div>
                <div class="hero-foot column style="height: 76px">
                  <form id = "interact">
                      <div class="field is-grouped">
                        <p class="control is-expanded">
                          <input class="input" type="text" id="userIn" placeholder="Type in a message">
                        </p>
                        <p class="control">
                          <button id="respond" type="submit" class="button has-text-white-ter has-background-grey-dark">
                            Send
                          </button>
                        </p>
                        <p class="control">
                          <button id="restart" type="reset" class="button has-text-white-ter has-background-grey-dark">
                            Restart
                          </button>
                        </p>
                      </div>
                  </form>
                </div>
              </section>
            </div>
        </div>

        <script>
            function cleanupText(text) {{
               text = applySentenceCase(text.replace(/ +(\W)/g, "$1"));
               text = text.replace(/\' /g, "\'");
               text = text.replace(/ i /g, " I ");
               text = text.replace(/ i'/g, " I'");
               // text = applySentenceCase(text.replace(/ (i) /g, " I "));
               return text
            }}
            function applySentenceCase(str) {{
               return str.replace(/.+?[\.\?\!](\s|$)/g, function (txt) {{
                   return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
               }});
            }}

            // Use this function to start blenderbot and avoid user to have to type in begin
            function send_begin_msg_recursive() {{
                console.log("send_begin_recursive called");

                // Get the bot going without the need for the user to type begin
                fetch('/interact', {{
                    headers: {{ 'Content-Type': 'application/json' }}, method: 'POST', body: "begin" }} 
                ).then(response=>response.json()).then(data=>{{
                    console.log("interactive_web.py interact 1 response data=");
                    console.log(data);
                    // Asking to type begin so send another begin command 
                    if (!data.episode_done && data.text.indexOf("Welcome to the overworld for the ParlAI messenger chatbot demo. Please type") > -1) {{
                        console.log("interactive_web.py found string with begin and about to call send_begin_recursive recursively");
                        send_begin_msg_recursive();
                    }} else if (!data.episode_done && data.text.indexOf("Welcome to the ParlAI Chatbot demo. You are now paired with a bot - feel free to send a message") > -1) {{
                        console.log("interactive_web.py ready to chat 1...");
                        var parDiv = document.getElementById("parent");

                        // Change info for Model response
                        welcomeText = String(data.text);
                        console.log("welcomeText=");
                        console.log(welcomeText);
                        parDiv.append(createChatRow("BlenderBot", welcomeText));
                        parDiv.scrollTo(0, parDiv.scrollHeight);
                    }} else {{
                        console.log("interactive_web.py ready to chat 2...");
                        var parDiv = document.getElementById("parent");

                        // Change info for Model response
                        welcomeText = "Welcome.  You can now send me a message and I will respond interactively."
                        parDiv.append(createChatRow("BlenderBot", welcomeText));
                        parDiv.scrollTo(0, parDiv.scrollHeight);
                    }};
                }});
            }};
		
            function createChatRow(agent, text) {{
                var article = document.createElement("article");
                article.className = "media"

                var figure = document.createElement("figure");
                figure.className = "media-left";

                var span = document.createElement("span");
                span.className = "icon is-large";

                var icon = document.createElement("i");
                icon.className = "fas fas fa-2x" + (agent === "You" ? " fa-user " : agent === "BlenderBot" ? " fa-robot" : "");

                var media = document.createElement("div");
                media.className = "media-content";

                var content = document.createElement("div");
                content.className = "content";

                var para = document.createElement("p");
                var paraText = document.createTextNode(text);

                var strong = document.createElement("strong");
                strong.innerHTML = agent;
                var br = document.createElement("br");

                para.appendChild(strong);
                para.appendChild(br);
                para.appendChild(paraText);
                content.appendChild(para);
                media.appendChild(content);

                span.appendChild(icon);
                figure.appendChild(span);

                if (agent !== "Instructions") {{
                    article.appendChild(figure);
                }};

                article.appendChild(media);

                return article;
            }}
            document.getElementById("interact").addEventListener("submit", function(event){{
                event.preventDefault()
                var text = document.getElementById("userIn").value;
                document.getElementById('userIn').value = "";

                console.log("Sending text because submit button hit");
                console.log(text);

                var parDiv = document.getElementById("parent");
                parDiv.append(createChatRow("You", text));
                parDiv.scrollTo(0, parDiv.scrollHeight);

                fetch('/interact', {{
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    method: 'POST',
                    body: text
                }}).then(response=>response.json()).then(data=>{{
                    var parDiv = document.getElementById("parent");
                    text = cleanupText(data.text);

                    // Change info for Model response
                    parDiv.append(createChatRow("BlenderBot", text));
                    parDiv.scrollTo(0, parDiv.scrollHeight);
                }})
            }});
            document.getElementById("interact").addEventListener("reset", function(event){{
                event.preventDefault()
                var text = document.getElementById("userIn").value;
                document.getElementById('userIn').value = "";

                fetch('/reset', {{
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    method: 'POST',
                }}).then(response=>response.json()).then(data=>{{
                    var parDiv = document.getElementById("parent");

                    parDiv.innerHTML = '';
                    parDiv.append(createChatRow("Instructions", "Welcome. To chat just ask me a question or just say hello."));
                    parDiv.scrollTo(0, parDiv.scrollHeight);
                }})
            }});

            // Get the bot going without the need for the user to type begin
            send_begin_msg_recursive();
        </script>

    </body>
</html>
"""  # noqa: E501


class MyHandler(BaseHTTPRequestHandler):
    """
    Handle HTTP requests.
    """

    def _interactive_running(self, opt, reply_text):
        reply = {'episode_done': False, 'text': reply_text}
        print(f"interactive_web reply_text={reply_text}") 
        SHARED['agent'].observe(reply)
        model_res = SHARED['agent'].act()
        return model_res

    def do_HEAD(self):
        """
        Handle HEAD requests.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        print("HTTP POST Received")
        """
        Handle POST request, especially replying to a chat message.
        """
        if self.path == '/interact':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            model_response = self._interactive_running(
                SHARED.get('opt'), body.decode('utf-8')
            )

            # Cleanup text before displaying
            model_response = re.sub(r'\s([?.!"](?:\s|$))', r'\1', model_response)
            print(f'model_response={model_resposne}')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_str = json.dumps(model_response)
            self.wfile.write(bytes(json_str, 'utf-8'))
        elif self.path == '/reset':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            SHARED['agent'].reset()
            self.wfile.write(bytes("{}", 'utf-8'))
        else:
            return self._respond({'status': 500})

    def do_GET(self):
        print("HTTP GET Received")
        """
        Respond to GET request, especially the initial load.
        """
        paths = {
            '/': {'status': 200},
            '/favicon.ico': {'status': 202},  # Need for chrome
        }
        if self.path in paths:
            self._respond(paths[self.path])
        else:
            self._respond({'status': 500})

    def _handle_http(self, status_code, path, text=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = WEB_HTML.format(STYLE_SHEET, FONT_AWESOME)
        return bytes(content, 'UTF-8')

    def _respond(self, opts):
        response = self._handle_http(opts['status'], self.path)
        self.wfile.write(response)


def setup_interweb_args(shared):
    """
    Build and parse CLI opts.
    """
    parser = setup_args()
    parser.description = 'Interactive chat with a model in a web browser'
    parser.add_argument('--port', type=int, default=PORT, help='Port to listen on.')
    parser.add_argument(
        '--host',
        default=HOST_NAME,
        type=str,
        help='Host from which allow requests, use 0.0.0.0 to allow all IPs',
    )
    return parser


def shutdown():
    global SHARED
    if 'server' in SHARED:
        SHARED['server'].shutdown()
    SHARED.clear()


def wait():
    global SHARED
    while not SHARED.get('ready'):
        time.sleep(0.01)


def interactive_web(opt):
    global SHARED

    opt['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

    # Create model and assign it to the specified task
    agent = create_agent(opt, requireModelExists=True)
    agent.opt.log()
    SHARED['opt'] = agent.opt
    SHARED['agent'] = agent
    SHARED['world'] = create_task(SHARED.get('opt'), SHARED['agent'])

    MyHandler.protocol_version = 'HTTP/1.0'
    httpd = HTTPServer((opt['host'], opt['port']), MyHandler)
    SHARED['server'] = httpd
    logging.info('http://{}:{}/'.format(opt['host'], opt['port']))

    print("Sending init question")

    try:
        SHARED['ready'] = True
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


@register_script('interactive_web', aliases=['iweb'], hidden=True)
class InteractiveWeb(ParlaiScript):
    @classmethod
    def setup_args(cls):
        return setup_interweb_args(SHARED)

    def run(self):
        return interactive_web(self.opt)


if __name__ == '__main__':
    InteractiveWeb.main()
