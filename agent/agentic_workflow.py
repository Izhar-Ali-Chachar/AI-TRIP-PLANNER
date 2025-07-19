from langgraph.graph import StateGraph, END, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from config.config import Call_LLM
from tools.weather_info_tool import WeatherInfoTool
from tools.currency_conversion_tool import CurrencyConverterTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool
from tools.place_search_tool import PlaceSearchTool
from prompt_library.prompt import SYSTEM_PROMPT

class GraphBuilder:
    def __init__(self):
        self.model_loader = Call_LLM()
        self.llm = self.model_loader.llm

        self.tools = []

        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()

        self.tools.extend(
            self.weather_tools.weather_tool_list +
            self.place_search_tools.place_search_tool_list +
            self.calculator_tools.calculator_tool_list +
            self.currency_converter_tools.currency_converter_tool_list
        )


        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)

        self.graph = None
        
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self, state: MessagesState):
        """Main agent function"""
        user_messages = state["messages"]
        input_messages = [self.system_prompt] + user_messages
        response = self.llm_with_tools.invoke(input_messages)
        
        # Return the full list including the new response
        return {"messages": user_messages + [response]}


    
    def build_graph(self):
        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
        
    def __call__(self):
        return self.build_graph()