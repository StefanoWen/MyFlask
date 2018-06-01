var canvas = document.getElementById("canvas");
var cxt = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function Dot() {
    this.alive = true;
    this.x = Math.round(Math.random() * canvas.width);
    this.y = Math.round(Math.random() * canvas.height);
    this.diameter = Math.random() * 10.8;
    this.ColorData = {
        Red: Math.round(Math.random() * 255),
        Green: Math.round(Math.random() * 255),
        Blue: Math.round(Math.random() * 255)
    };
    this.alpha = 0.1;
    this.color = "rgba(" + this.ColorData.Red + ", " + this.ColorData.Green + "," + this.ColorData.Blue + "," + this.alpha + ")";
    this.velocity = {
        x: Math.round(Math.random() < 0.5 ? -1 : 1) * Math.random() * 0.7,
        y: Math.round(Math.random() < 0.5 ? -1 : 1) * Math.random() * 0.7
    }
}

Dot.prototype = {
    Draw: function () {
        cxt.fillStyle = this.color;
        cxt.beginPath();
        cxt.arc(this.x, this.y, this.diameter, 0, Math.PI * 2, false);
        cxt.fill()
    }, Update: function () {
        if (this.alpha < 0.8) {
            this.alpha += 0.01;
            this.color = "rgba(" + this.ColorData.Red + ", " + this.ColorData.Green + "," + this.ColorData.Blue + "," + this.alpha + ")"
        }
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        if (this.x > canvas.width + 5 || this.x < 0 - 5 || this.y > canvas.height + 5 || this.y < 0 - 5) {
            this.alive = false
        }
    }
};
var Event = {
    rArray: [], Init: function () {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        for (var x = 0; x < 150; x++) {
            this.rArray.push(new Dot())
        }
        this.Update()
    }, Draw: function () {
        cxt.clearRect(0, 0, canvas.width, canvas.height);
        this.rArray.forEach(function (dot) {
            dot.Draw()
        })
    }, Update: function () {
        if (Event.rArray.length < 150) {
            for (var x = Event.rArray.length; x < 150; x++) {
                Event.rArray.push(new Dot())
            }
        }
        Event.rArray.forEach(function (dot) {
            dot.Update()
        });
        Event.rArray = Event.rArray.filter(function (dot) {
            return dot.alive
        });
        Event.Draw();
        requestAnimationFrame(Event.Update)
    }
};
window.onresize = function () {
    Event.rArray = [];
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight
};
Event.Init();