from flitscore.models import *

# needed for registering to developer.salesforce.com

saucedemo = {"url": obj(objtype="chrome", input="https://www.saucedemo.com/"),
             "users":
             {
    "standard_user": {"username": "standard_user", "name": "Standard User", "secret": "secret_sauce"},
    "locked_out_user": {"username": "locked_out_user", "name": "Lockedout User", "secret": "secret_sauce"},
    "problem_user": {"username": "problem_user", "name": "Problem User", "secret": "secret_sauce"},
    "performance_glitch_user": {"username": "performance_glitch_user", "name": "Performanceglitch User", "secret": "secret_sauce"},
}
}
