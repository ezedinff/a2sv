# Game Station

## Problem
design a game station, which can play different games.
games are added dynamically like a plugin. (like vs code extension)

## Solution
## Simple Game using Canvas
```typescript

// Game.ts
interface Game {
    name: string;
    init(rootID: string): void;
    play(): void;
    stop(): void;
}

// GameStation.ts
class GameStation {
    private gamesMap: Map<string, Game> = new Map();
    private currentGame: Game | null = null;
    private static readonly rootID = 'game-root'; // component id on dom
    addGame(game: Game) {
        this.gamesMap.set(game.name, game);
    }
    play(gameName: string) {
        if (this.currentGame) {
            this.currentGame.stop();
        }
        const game = this.gamesMap.get(gameName);
        if (game) {
            this.currentGame = game;
            game.init(this.rootID);
            game.play();
        }
    }
}

// ShootingGamePlugin.ts
class ShootingGamePlugin {
    constructor(private gameStation: GameStation) {}
    register(game: Game) {
        this.gameStation.addGame(game);
    }
}

// ShootingGame.ts
class ShootingGame implements Game {
    name = 'shooting';
    private canvas: HTMLCanvasElement;
    private playerTank: Tank;
    init(rootID: string) {
        this.canvas = document.createElement('canvas');
        this.canvas.width = 500;
        this.canvas.height = 500;
        document.getElementById(rootID).appendChild(this.canvas);

        const ctx = this.canvas.getContext('2d');
        if (ctx) {
            this.playerTank = new Tank(0, 0, 100, 100);
            this.playerTank.draw(ctx);
        }

        
    }
    play() {
        // start game


    }
    stop() {
        // stop game
    }
}

// Tank.ts
class Tank {
    private x: number;
    private y: number;
    private width: number;
    private height: number;
    private color: string;
    private speed: number;
    private ctx: CanvasRenderingContext2D;
    constructor(x: number, y: number, width: number, height: number, color: string, speed: number, ctx: CanvasRenderingContext2D) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
        this.speed = speed;
        this.ctx = ctx;
    }
    draw(ctx: CanvasRenderingContext2D) {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
    move(x: number, y: number) {
        this.x = x;
        this.y = y;
    }

    fire() {
        const bullet = new Bullet(this.x, this.y, 10, 10, 'red', 10);
        bullet.fire(this.ctx);
    }
}

// bullet.ts
class Bullet {
    private x: number;
    private y: number;
    private width: number;
    private height: number;
    private color: string;
    private speed: number;
    constructor(x: number, y: number, width: number, height: number, color: string, speed: number) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
        this.speed = speed;
    }
    draw(ctx: CanvasRenderingContext2D) {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
    move() {
        this.x = this.x + this.speed;
    }
    fire(ctx: CanvasRenderingContext2D) {
        // clear rect from canvas
        ctx.clearRect(this.x, this.y, this.width, this.height);
        this.draw(ctx);
        this.move();
    }
}

// EnemyTank.ts


// main.ts
const gameStation = new GameStation();
const shootingGamePlugin = new ShootingGamePlugin(gameStation);
shootingGamePlugin.register(new ShootingGame());
gameStation.play('shooting');

```