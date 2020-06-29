using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
  public new static void UpdatePosition(string key, out int x, out int y)
  {
  switch (key)
   {
    case "DownArrow":
      x = 0;
      y = 1;
      break;
    case "UpArrow":
      x = 0;
      y = -1;
      break;
    case "LeftArrow":
      x = -1;
      y = 0;
      break;
    case "RightArrow":
      x = 1;
      y = 0;
      break;
    default:
      x = 0;
      y = 1;
      break;
   }
  }
  public new static char UpdateCursor(string key){
switch (key)
   {
    case "DownArrow":
      return '⌵';
      break;
    case "UpArrow":
      return '^';
      break;
    case "LeftArrow":
      return '<';
      break;
    case "RightArrow":
      return '>';
      break;
    default:
      return '<';
      break;
  }
 }
 public new static int KeepInBounds(int Coordinate, int MaxValue)
 {
   if(Coordinate < 0)
   {
     return 0;
   }
    else if(Coordinate >=  MaxValue)
    {
      return MaxValue -1;
    } 
    else {
      return Coordinate;
    }
   }
   public new static bool DidScore(int charx, int chary,int fruitx, int fruity){
if(charx == fruitx && chary == fruity){
  return true;
} else {
  return false;
}
   }
 }
}

