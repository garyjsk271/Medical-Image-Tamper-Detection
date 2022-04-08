
import matplotlib.pyplot as plt

epochs = [i for i in range(1,201)]
acc = []
train_loss = []
val_acc = []
val_loss = []
with open('output.txt', 'r') as f:
    log = f.readlines()
    for line in log:
        if len(line) < 63:
            continue
        train_loss.append(float(line[6:12]))
        acc.append(float(line[20:26]) )
        val_loss.append(float(line[38:45]) )
        val_acc.append(float(line[57:]) )

fig, ax = plt.subplots(1, 2, figsize=(20, 3))
ax = ax.ravel()

for i in range(2):
    if i == 0:
        ax[i].plot(acc)
        ax[i].plot(val_acc)
        ax[i].set_title("Model Accuracy")
        ax[i].set_xlabel("epochs")
        ax[i].set_ylabel("accuracy")
        ax[i].legend(["train", "validation"])
    else:
        ax[i].plot(train_loss)
        ax[i].plot(val_loss)
        ax[i].set_title("Model Loss")
        ax[i].set_xlabel("epochs")
        ax[i].set_ylabel("loss")
        ax[i].legend(["train", "validation"])

plt.show()

