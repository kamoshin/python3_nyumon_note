def route(start, end, *args):
    route_list = [start]
    route_list += list(args)
    route_list += [end]
    route_str = "→".join(route_list)
    print(route_str)

start = "東京"
end = "宮崎"
route(start, end, "神戸", "長崎", "熊本")
