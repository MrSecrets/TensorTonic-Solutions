def retraining_policy(daily_stats, config):
    """
    Decide which days to trigger model retraining.
    """
    budget = config["budget"]
    retrain_cost = config["retrain_cost"]
    cooldown = config["cooldown"]

    retrain_days = []
    days_since_retrain  = 1
    start = True
    for days in daily_stats:
        if budget<retrain_cost:
            break

        retrain = False
        # if days_since_retrain >=config["max_staleness"]:
        #     retrain = True

        if days_since_retrain >=cooldown or start:
            if days["drift_score"]>config["drift_threshold"]:
                retrain = True
            elif days["performance"]<config["performance_threshold"]:
                retrain = True
            elif days_since_retrain >=config["max_staleness"]:
                retrain = True

        if retrain:
            retrain_days.append(days["day"])
            budget -= retrain_cost
            days_since_retrain  = 0
            start = False
        # else:
        days_since_retrain  +=1
    # print(daily_stats)
    # print(config)
    # print(retrain_days)
    return sorted(retrain_days)


