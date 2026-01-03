module Main exposing (..)

import Browser
import File exposing (File)
import File.Select as Select
import Html exposing (Html, button, text, div, pre, code)
import Html.Attributes exposing (style)
import Html.Events exposing (onClick)
import Task

type alias Product =
  { x : Int
  , y : Int
  }

type Inst = Mul Int Int
--                               current   input             new current    rest
type alias Parser = List Inst -> List Char -> List Char -> (List Inst, List Char, List Char)

expect : Char -> Parser
expect ch parsed cur input =
  case (List.head input, List.tail input) of
    (Just head, Just tail) ->
      if head == ch then
        (parsed, head :: cur, tail)
      else
        (parsed, [], tail)
    _ -> (parsed, [], [])

getInt : Parser
getInt parsed cur input =
  case (List.head input, List.tail input) of
    (Just head, Just tail) ->
      case (head |> String.fromChar |> String.toInt) of
        Just _ -> getInt parsed (head :: cur) tail
        Nothing ->
          if head == ',' then
            (parsed, cur, input)
          else if head == ')' then
            let parts = String.split "," (String.fromList cur) in
                case (List.head parts) of
                  (Just first) ->
                    case (List.head first) of
                      (Just second) ->
                        case (String.toInt first, String.toInt second) of
                          (Just a, Just b) -> (Mul a b :: parsed, [], tail)
                          _ -> (parsed, [], tail)
                      _ -> (parsed, [], tail)
                  _ -> (parsed, [], tail)
          else
            (parsed, [], input)
    _ -> (parsed, [], [])

andThen : Parser -> Parser -> Parser
andThen pB pA parsed cur input =
  case pA parsed cur input of
    (a, b, rest) -> pB a b rest

part1Parser : Parser
part1Parser =
  expect 'm'
  |> andThen (expect 'u')
  |> andThen (expect 'l')
  |> andThen (expect '(')
  |> andThen getInt

part1 : String -> List Inst
part1 str =
  let (a, _, _) = part1Parser [] [] (String.toList str) in
      a


---------------------------------------------------

main : Program () Model Msg
main =
  Browser.element
    { init = init
    , view = view
    , update = update
    , subscriptions = subscriptions
    }

type alias Model =
  { input : Maybe String
  , output : String
  }


init : () -> (Model, Cmd Msg)
init _ =
  ( Model Nothing "Waiting for input", Cmd.none )

type Msg
  = NewInput
  | InputSelected File
  | InputLoaded String

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    NewInput -> (model, Select.file [] InputSelected)
    InputSelected file -> (model, Task.perform InputLoaded (File.toString file))
    InputLoaded content ->
      ({ model
       | input = Just content
       , output = Debug.toString (run statements content)
       } , Cmd.none)

view : Model -> Html Msg
view model =
  case model.input of
    Nothing ->
      button [ onClick NewInput ] [ text "Load input" ]

    Just content ->
      div [] [
        button [ onClick NewInput ] [ text "Load new input" ]
        , pre [ style "text-wrap" "auto", style "margin-bottom" "4rem" ] [ code [] [text model.output] ]
        , pre [ style "text-wrap" "auto" ] [ code [] [text content] ]
        ]



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions _ =
  Sub.none
